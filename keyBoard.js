function keyBoard(word) {
    let ans = 0
    let k = 1
    for (let i = 0; i < word.length; i ++) {
        if (i >= 8) {
            k = 2
        }
        if (i >= 16) {
            k = 3
        }
        if (i >= 24) {
            k = 4
        }
        ans += k
    }
    return ans
}


const word = "abcdefghijklmnopqrstuvwx"
const ans = keyBoard(word)
console.log(ans)