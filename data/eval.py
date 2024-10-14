import openai, json, os


# your openai api key
API_KEY = os.getenv('OPENAI_API_KEY')
# path to "data.json"
ANSWER_PATH = os.getenv('ANSWER_PATH')
# path to your output
OUTPUT_PATH = os.getenv('OUTPUT_PATH')

PROMPT = '''
Please evaluate the output of models based on the given question and groundtruth and tell me whether the output is right.

Please pay attention to the following rules:
1. The output contains rationale of the reasoning process and answer which is summarized from the reasoning process. Please extract the answer from the output and make your judgement only based on answer, NOT rationale.
2. The answer is right if it follows the question in meaning and be consistent with the groundtruth.
3. Do not be too strict about the answer. Format different from the groundtruth and minor grammar issues are allowed.
If you think the answer is correct according to the groundtruth, please output "right", otherwise output "wrong". You can only print "right" or "wrong" and nothing else.

Here is the question: {}
Here is the groundtruth: {}
Here is the output: {}
'''

client = openai.OpenAI(api_key = API_KEY)

def get_response(question, groundtruth, output):
    response = client.chat.completions.create(
        messages = [{
            'role': 'user',
            'content': PROMPT.format(question, groundtruth, output)
        }],
        model = 'gpt-4-turbo-preview'
    )
    return response.choices[0].message.content


with open(ANSWER_PATH, 'r') as fp:
    answers = json.load(fp)

answers = dict(zip([entry['id'] for entry in answers], answers))

with open(OUTPUT_PATH, 'r') as fp:
    outputs = json.load(fp)

acc_p = {
    'Location and Orientation': [0, 0],
    'Temporal Information': [0, 0],
    'Cultural Background': [0, 0],
    'Attributes': [0, 0],
    'Relationships': [0, 0],
    'All': [0, 0]
}
acc_q = {
    'Location and Orientation': [0, 0],
    'Temporal Information': [0, 0],
    'Cultural Background': [0, 0],
    'Attributes': [0, 0],
    'Relationships': [0, 0],
    'All': [0, 0]
}
for entry in outputs:
    question = answers[entry['id']]['question']
    answer_1 = answers[entry['id']]['answer']['answer_1']
    answer_2 = answers[entry['id']]['answer']['answer_2']
    output_1 = entry['output']['output_1']
    output_2 = entry['output']['output_2']
    response_1 = 1 if 'right' in get_response(question, answer_1, output_1) else 0
    response_2 = 1 if 'right' in get_response(question, answer_2, output_2) else 0
    acc_p[answers[entry['id']]['category']][0] += response_1 * response_2
    acc_q[answers[entry['id']]['category']][0] += response_1 + response_2
    acc_p[answers[entry['id']]['category']][1] += 1
    acc_q[answers[entry['id']]['category']][1] += 2
    acc_p['All'][0] += response_1 * response_2
    acc_q['All'][0] += response_1 + response_2
    acc_p['All'][1] += 1
    acc_q['All'][1] += 2

print('Acc_p')
for k, v in acc_p.items():
    print(k + ': ' + str(v[0] / v[1]))
print('\nAcc_q')
for k, v in acc_q.items():
    print(k + ': ' + str(v[0] / v[1]))
