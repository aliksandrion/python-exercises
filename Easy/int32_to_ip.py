def int32_to_ip(int32):
    data = []
    for i in range(4):  # convert from integer to a 32-bit number
        data.append(str(int32 % 256))
        int32 = int32 // 256
    return '.'.join(data[::-1])  # return the list backwards with network and host numbers


# test
assert int32_to_ip(32) == "0.0.0.32"

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
