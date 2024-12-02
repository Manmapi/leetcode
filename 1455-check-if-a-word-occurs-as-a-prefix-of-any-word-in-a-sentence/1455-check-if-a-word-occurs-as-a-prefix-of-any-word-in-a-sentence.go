func isPrefixOfWord(sentence string, searchWord string) int {
    for i, word := range strings.Split(sentence, " ") {
        fmt.Println(word, strings.HasPrefix(word, searchWord))
        if strings.HasPrefix(word, searchWord) {
            return i + 1
        }
    }
    return -1
}