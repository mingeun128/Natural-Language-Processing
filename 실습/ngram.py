def n_gram(text, n):
    words = text.split()
    result = []
    for i in range(len(words)-n+1):
        result.append(' '.join(words[i:i+n]))
    return result

stext = "Colaboratory(또는 줄여서 'Colab')를 사용하면 브라우저에서 Python을 작성하고 실행할 수 있습니다."
ngrams = n_gram(stext,4)
print(ngrams)
