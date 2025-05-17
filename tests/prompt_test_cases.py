from llm_mocks import MockLLM


def test_llm_factual_answer_canadian_capital():
    llm = MockLLM()
    response = llm.invoke("What is the capital of Canada?")
    assert "Ottawa" in response


def test_llm_structured_json_output():
    llm = MockLLM()
    response = llm.invoke("Please return JSON with status info.")
    assert response.startswith("{") and response.endswith("}")
    assert '"status": "ok"' in response


def test_llm_markdown_formatting_response():
    llm = MockLLM()
    response = llm.invoke("Please respond in Markdown format.")
    assert "#" in response or "**" in response
