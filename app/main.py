if __name__ == '__main__':
    import uvicorn
    uvicorn.run('fess_text_vectorizer.app:app',
                host='0.0.0.0', port=8900, reload=True)
