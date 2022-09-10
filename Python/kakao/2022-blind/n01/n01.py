def solution(id_list, report, k):
    report_cnt = {x: set() for x in id_list}
    for r in report:
        a, b = r.split()
        report_cnt[b].add(a)

    answer_dic = {x: 0 for x in id_list}
    for r, ids in report_cnt.items():
        if len(ids) < k:
            continue
        for i in ids:
            answer_dic[i] += 1

    return list(answer_dic.values())


if __name__ == '__main__':
    print(solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2)
    )
