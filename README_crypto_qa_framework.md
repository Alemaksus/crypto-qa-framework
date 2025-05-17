# 🧪 Crypto QA Framework

A lightweight QA framework for validating prompt-based LLM responses using Python, PyTest, and a simulated `MockLLM` agent.  
Designed to enable fast and reliable testing of AI agents without requiring external API access (e.g., OpenAI).

---

## 🚀 Key Features

- ✅ **Mock-based testing** without OpenAI API
- 🧠 **Prompt QA validation** for factual, structured, and formatted responses
- ⚙️ **CI/CD friendly** – run anywhere with Python and PyTest
- 📦 Easy to extend for JSON, Markdown, logic or classification use cases

---

## 📁 Project Structure

```
crypto-qa-framework/
├── data/                       # Optional data assets (CSV, etc.)
├── llm_mocks/
│   └── mock_llm.py            # MockLLM simulating model behavior
├── tests/
│   └── prompt_test_cases.py   # PyTest unit tests for prompts
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

---

## 🧩 Example: `MockLLM`

```python
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
```

---

## ✅ Tests Included

### `prompt_test_cases.py`:

- `test_llm_factual_answer_canadian_capital()`  
  → Validates factual knowledge

- `test_llm_structured_json_output()`  
  → Validates structured response format

- `test_llm_markdown_formatting_response()`  
  → Validates Markdown-style formatting

```bash
$ pytest tests/prompt_test_cases.py
...
3 passed in 0.01s
```

---

## 💡 Use Cases

- Testing prompt-response logic **offline**
- Validating fallback agents in LLM-based systems
- Educational environments where API cost/availability is limited
- Preparing test scaffolding before model integration

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/crypto-qa-framework.git
cd crypto-qa-framework
pip install -r requirements.txt
pytest
```

---

## 🔮 Roadmap

- [ ] Add CLI test runner
- [ ] Generate Markdown test reports
- [ ] Extend test cases to handle hallucinations, edge cases, and multilingual prompts

---

## 🧑‍💻 Author

**Aleksandr M.** – QA Automation Engineer focused on AI systems testing, LangChain workflows, and test strategy for LLMs.