N, M = list(map(int, input().split()))

if N > M:
  if N - M == 1:
    print("Dr. Chaz needs {0} more piece of chicken!".format(N - M))
  else:
    print("Dr. Chaz needs {0} more pieces of chicken!".format(N - M))
elif N < M:
  if M - N == 1:
    print("Dr. Chaz will have {0} piece of chicken left over!".format(M - N))
  else:
    print("Dr. Chaz will have {0} pieces of chicken left over!".format(M - N))
