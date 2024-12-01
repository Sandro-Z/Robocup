def josephus_problem(n, k):
    people = list(range(1, n + 1))
    index = 0
    while len(people) > 1:
        index = (index + k - 1) % len(people)
        people.pop(index)
    return people[0]

n = 233
k = 3
last_person = josephus_problem(n, k)
print(f"The last person remaining is originally numbered {last_person}.")