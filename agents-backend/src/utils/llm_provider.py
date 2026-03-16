"""
Unified LLM Provider Factory

Supports multiple LLM providers:
  - OpenAI (via API key and/or base URL)
  - Azure OpenAI (via Azure endpoint, deployment, version)
  - Groq (via Groq API)
  - Google Gemini (via Google API key or OpenAI-compatible endpoint)
  - Any OpenAI-compatible provider (via custom base URL)

Configuration via environment variables:
  - LLM_PROVIDER: 'openai', 'azure', 'groq', 'google', or 'custom'
  - LLM_MODEL: Model name (e.g., 'gpt-4', 'claude-3-5-sonnet', 'mixtral-8x7b-32768')
  - OPENAI_API_KEY: API key for OpenAI / Groq / Google compatible endpoints
  - OPENAI_BASE_URL: Base URL for OpenAI-compatible endpoints
  
  For Azure OpenAI:
    - AZURE_ENDPOINT: Your Azure endpoint URL
    - AZURE_CHAT_DEPLOYMENT: Deployment name for chat models
    - AZURE_CHAT_VERSION: API version (e.g., '2024-02-01')
  
  For Groq:
    - GROQ_API_KEY: Groq API key (same as OPENAI_API_KEY if set)
  
  For Google Gemini:
    - GOOGLE_API_KEY: Google Gemini API key
    - Or use OpenAI-compatible endpoint if provided
"""

import os
from typing import Optional
from langchain_core.language_models.chat_models import BaseChatModel
from dotenv import load_dotenv

load_dotenv()


def get_llm(
    temperature: float = 0,
    provider: Optional[str] = None,
    model: Optional[str] = None,
) -> BaseChatModel:
    """
    Factory function to get a configured LLM instance.
    
    Args:
        temperature: Model temperature (0-1)
        provider: LLM provider ('openai', 'azure', 'groq', 'google', 'custom', or None for auto-detect)
        model: Model name (overrides env var)
    
    Returns:
        A configured BaseChatModel instance
    
    Raises:
        ValueError: If provider is unsupported or required credentials are missing
    """
    # Determine provider and model from args or env vars
    llm_provider = (provider or os.getenv("LLM_PROVIDER", "openai")).lower()
    llm_model = model or os.getenv("LLM_MODEL", "gpt-4o-mini")
    
    print(f"LLM Provider: {llm_provider}, Model: {llm_model}, Temperature: {temperature}")
    
    if llm_provider == "azure":
        return _get_azure_openai(llm_model, temperature)
    elif llm_provider == "groq":
        return _get_groq(llm_model, temperature)
    elif llm_provider == "google":
        return _get_google_gemini(llm_model, temperature)
    elif llm_provider == "custom" or llm_provider == "openai":
        # Try OpenAI-compatible endpoint first, then fallback to direct OpenAI
        base_url = os.getenv("OPENAI_BASE_URL")
        if base_url:
            return _get_openai_compatible(llm_model, base_url, temperature)
        else:
            return _get_openai(llm_model, temperature)
    else:
        raise ValueError(
            f"Unsupported LLM provider: {llm_provider}. "
            f"Supported: 'openai', 'azure', 'groq', 'google', 'custom'"
        )


def _get_openai(model: str, temperature: float) -> BaseChatModel:
    """Get OpenAI ChatGPT instance."""
    from langchain_openai import ChatOpenAI
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is required for OpenAI provider")
    
    return ChatOpenAI(
        model=model,
        temperature=temperature,
        openai_api_key=api_key,
    )


def _get_openai_compatible(model: str, base_url: str, temperature: float) -> BaseChatModel:
    """Get OpenAI-compatible LLM instance (e.g., local server, custom API)."""
    from langchain_openai import ChatOpenAI
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is required for OpenAI-compatible provider"
        )
    
    return ChatOpenAI(
        model=model,
        temperature=temperature,
        base_url=base_url,
        api_key=api_key,
    )


def _get_azure_openai(model: str, temperature: float) -> BaseChatModel:
    """Get Azure OpenAI instance."""
    from langchain_openai import AzureChatOpenAI
    
    azure_endpoint = os.getenv("AZURE_ENDPOINT")
    azure_deployment = os.getenv("AZURE_CHAT_DEPLOYMENT")
    azure_api_version = os.getenv("AZURE_CHAT_VERSION", "2024-02-01")
    api_key = os.getenv("AZURE_OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
    
    if not azure_endpoint:
        raise ValueError("AZURE_ENDPOINT environment variable is required for Azure OpenAI")
    if not azure_deployment:
        raise ValueError("AZURE_CHAT_DEPLOYMENT environment variable is required for Azure OpenAI")
    if not api_key:
        raise ValueError(
            "AZURE_OPENAI_API_KEY or OPENAI_API_KEY environment variable is required for Azure OpenAI"
        )
    
    return AzureChatOpenAI(
        azure_endpoint=azure_endpoint,
        azure_deployment=azure_deployment,
        openai_api_version=azure_api_version,
        api_key=api_key,
        temperature=temperature,
    )


def _get_groq(model: str, temperature: float) -> BaseChatModel:
    """Get Groq LLM instance."""
    try:
        from langchain_groq import ChatGroq
    except ImportError:
        raise ImportError(
            "langchain-groq is required for Groq provider. Install with: pip install langchain-groq"
        )
    
    api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY or OPENAI_API_KEY environment variable is required for Groq provider"
        )
    
    return ChatGroq(
        model=model,
        temperature=temperature,
        groq_api_key=api_key,
    )


def _get_google_gemini(model: str, temperature: float) -> BaseChatModel:
    """Get Google Gemini instance."""
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
    except ImportError:
        raise ImportError(
            "langchain-google-genai is required for Google Gemini provider. "
            "Install with: pip install langchain-google-genai"
        )
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is required for Google Gemini provider")
    
    return ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        google_api_key=api_key,
    )
