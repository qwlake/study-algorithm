function solution(arrangement) {
    let stack = 0;
    let close = false;
    let answer = 0;
    for (let i = 0; i < arrangement.length; i++) {
        if (arrangement[i] === "(") {
            stack += 1;
            close = true;
        } else if (close) {
            stack -= 1;
            answer += stack;
            close = false;
        } else {
            stack -= 1;
            answer += 1;
        }
        // console.log(i, arrangement.slice(0,i+1), stack, answer);
    }
    return answer;
}

console.log(solution("()(((()())(())()))(())"));