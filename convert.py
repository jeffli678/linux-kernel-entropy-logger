import struct
import re

def to_binary(result):

    # struct {
		# long jiffies;
		# unsigned cycles;
		# unsigned num;
	# } sample;

    j, c, n = result
    j = int(j)
    c = int(c)
    n = int(n)

    binary = b''
    # binary += struct.pack('q', j)[:4]
    binary += struct.pack('q', j)
    binary += struct.pack('I', c)
    binary += struct.pack('I', n)

    # each data point should be 16 bytes long
    # assert len(binary) == 16
    
    return binary

log = open('log-10w.txt').read().splitlines()
output = open('output.bin', 'wb')

count = 0

# [   10.068375] rnd log 5314: 4294894814, 3259496115, 8388864

for line in log:


    if not 'rnd log' in line:
        continue

    count += 1

    if count > 200000 and count <= 300000:
        result = re.match(r'.* rnd log \d+: (\d+), (\d+), (\d+)', line)
        
        result = result.groups(1)
        
        output.write(to_binary(result))


output.close()