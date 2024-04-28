# question-answering usecase
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

# Define a list of common IT issues and corresponding context
it_issues = [
    {
        "issue": "How to fix a slow computer?",
        "context": "If your computer is running slow, you can try clearing temporary files, uninstalling unnecessary programs, or upgrading your hardware components like RAM or SSD."
    },
    {
        "issue": "How to troubleshoot network connectivity issues?",
        "context": "If you're experiencing network connectivity issues, you can check if your router is properly connected, restart your modem, or try resetting your network settings on your device."
    },
    {
        "issue": "How to resolve 'No Internet Access' error?",
        "context": "If you're seeing a 'No Internet Access' error, you can try restarting your router and modem, checking your network cables, or resetting your network settings on your device."
    }
]

# Function to provide technical support using the QA model
def provide_technical_support(issue, context):
    answer = qa_pipeline(question=issue, context=context)
    return answer['answer']

issue_to_resolve = "How to fix a slow computer?"
context_for_issue = next(item['context'] for item in it_issues if item['issue'] == issue_to_resolve)
solution = provide_technical_support(issue_to_resolve, context_for_issue)

print(f"Solution for '{issue_to_resolve}': {solution}")
