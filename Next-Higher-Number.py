def next_bigger(n):
    stringList = list(str(n)[::-1])
    for i in range(len(stringList)):
      if i == len(stringList) - 1:
        return -1
      j = i + 1
      if stringList[i] > stringList[j]:
        left, right = stringList[:j], stringList[j:]
        for k in range(len(sorted(left))):
          if left[k] > right[0]:
            left[k], right[0] = right[0], left[k]
            break
        result = int(''.join(str(i) for i in reversed(sorted(left, reverse = True) + right)))
        return result
