from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=250
    )
    result = response.choices[0].message.get("content", "")
    return result


@app.route('/generateContent', methods=['GET', 'POST'])
def generate_content():
    if request.method == 'POST':
        user_input = request.json.get('user_input')
        if user_input:
            prompt = f"Generate a content for engaging social media post to captivate our audience and drive interest" \
                     f"in the product, which is delimited with triple " \
                     f"backticks?\n\nContent: ```{user_input}```"
            result = get_completion(prompt)
            return jsonify(result=result)
        else:
            return jsonify(result="I'm sorry, but there is no content "
                                  "Can you please provide the content?")
    return jsonify(result=None)


@app.route('/analyzeSentiment', methods=['GET', 'POST'])
def analyze_sentiment():
    if request.method == 'POST':
        user_input = request.json.get('user_input')
        prompt = request.json.get('prompt')
        if user_input and prompt:
            prompt += f"\n\nReview text: ```{user_input}```"
            result = get_completion(prompt)
            return jsonify(result=result)
        else:
            return jsonify(result="I'm sorry, but there is no review text provided. Can you please provide the review "
                                  "text?")
    return jsonify(result=None)


@app.route('/summarization', methods=['GET', 'POST'])
def summarization():
    if request.method == 'POST':
        user_input = request.json.get('user_input')
        prompt = request.json.get('prompt')
        if user_input and prompt:
            prompt = f"\n\nContent: ```{user_input}```"
            result = get_completion(prompt)
            return jsonify(result=result)
        else:
            return jsonify(result="I'm sorry, but there is no content "
                                  "Can you please provide the content?")
    return jsonify(result=None)


@app.route('/generateResponse', methods=['GET', 'POST'])
def generate_response():
    if request.method == 'POST':
        user_input = request.json.get('user_input')
        if user_input:
            prompt = f"Generate an short email response in 130 words to the customer for the feedback given by the " \
                     f"customer of the following content, " \
                     f"which is delimited with triple backticks?\n\nContent: ```{user_input}```"
            result = get_completion(prompt)
            return jsonify(result=result)
        else:
            return jsonify(result="I'm sorry, but there is no content "
                                  "Can you please provide the content?")
    return jsonify(result=None)


if __name__ == '__main__':
    # Set your OpenAI API key
    # openai.api_key = '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' #mine
    openai.api_key = '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' #shaip
    app.run(debug=True)
