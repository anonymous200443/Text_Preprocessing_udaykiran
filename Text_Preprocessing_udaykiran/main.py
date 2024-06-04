# main.py

from Text_Processing import (
    load_data,
    char_counts,
    word_counts,
    stop_words_length,
    numeric_count,
    upper_case_count,
    cont_to_exp,
    remove_punctuation,
    remove_extra_spaces,
    remove_html,
    remove_accented_chars,
    lemmatize_text,
    tokenize_text,
    get_noun_chunks,
    detect_language,
    correct_spelling,
    create_wordcloud,
    get_sentiment
)

if __name__ == "__main__":
    df = load_data('Twitter_Data.csv')
    df['word_counts'] = df['chat'].apply(word_counts)
    df['char_counts'] = df['sentiment'].apply(lambda x: char_counts(str(x)))
    df['stop_words_length'] = df['chat'].apply(stop_words_length)
    df['numeric_count'] = df['sentiment'].apply(numeric_count)
    df['upper_case_count'] = df['sentiment'].apply(upper_case_count)
    df['chat'] = df['chat'].apply(cont_to_exp)
    df['chat'] = df['chat'].apply(remove_punctuation)
    df['chat'] = df['chat'].apply(remove_extra_spaces)
    df['chat'] = df['chat'].apply(remove_html)
    df['chat'] = df['chat'].apply(remove_accented_chars)
    df['chat'] = df['chat'].apply(lemmatize_text)
    df['tokenized_chat'] = df['chat'].apply(tokenize_text)
    df['noun_chunks'] = df['chat'].apply(get_noun_chunks)
    df['language'] = df['chat'].apply(detect_language)
    df['corrected_chat'] = df['chat'].apply(correct_spelling)

    # Example word cloud
    text = ' '.join(df['chat'])
    create_wordcloud(text)

    print(df.head())
