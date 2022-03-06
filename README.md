# Sentence Encoding/Embedding Serving Server for Fess

## Getting Started

### Run Docker

```
docker run -p 8900:8900 -it ghcr.io/codelibs/fess-text-vectorizer:snapshot
```

### Request

```
curl -s -H "Content-Type:application/json" -XPOST localhost:8900/vectorize -d '
{
  "data": [
    {
      "lang": "en",
      "content": "This is a pen."
    },
    {
      "lang": "ja",
      "content": "今日の天気は晴れです。"
    }
  ]
}
'
```

## Build

### Build Docker

```
docker build --rm -t ghcr.io/codelibs/fess-text-vectorizer:snapshot .
```

