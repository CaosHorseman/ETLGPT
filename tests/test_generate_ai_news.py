import importlib
import sys
import types
from pathlib import Path
from unittest.mock import Mock, patch


def test_generate_ai_news_returns_short_string():
    openai_stub = types.SimpleNamespace()
    openai_stub.ChatCompletion = Mock()
    openai_stub.ChatCompletion.create.return_value = Mock(
        choices=[Mock(message=Mock(content="Mensagem de teste"))]
    )
    with patch.dict(sys.modules, {"openai": openai_stub}):
        sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
        news = importlib.import_module("news")
        importlib.reload(news)
        result = news.generate_ai_news({"name": "Joao"})
        assert isinstance(result, str)
        assert len(result) <= 100

