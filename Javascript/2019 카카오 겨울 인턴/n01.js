function solution(board, moves) {
    let answer = 0;
    let basket = [];
    let pick;
    let idx;
    moves.forEach(e => {
        idx = 0;
        while (idx < board.length && board[idx][e-1] === 0) {
            idx++;
        }
        if (idx !== board.length) {
            pick = board[idx][e-1];
            board[idx][e-1] = 0;
            if (basket[basket.length-1] === pick) {
                basket.pop();
                answer++;
            } else {
                basket.push(pick);
            }
        }
    });
    return answer*2;
}

console.log(solution(
    [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
    [1,5,3,5,1,2,1,4]
));