string_ABCD = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'
print(sum(list(map(lambda x : ord('E') - ord(x), string_ABCD))))