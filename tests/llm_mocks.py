class MockLLM:
    """
    Simulated LLM for testing prompt-based responses without using OpenAI API.
    """

    def invoke(self, prompt: str) -> str:
        prompt_lower = prompt.lower()
        if "capital of canada" in prompt_lower:
            return "Ottawa is the capital of Canada."
        elif "return json" in prompt_lower:
            return '{"status": "ok", "country": "Canada"}'
        elif "markdown" in prompt_lower:
            return "# Welcome\nThis is a markdown response."
        return "Unknown"
