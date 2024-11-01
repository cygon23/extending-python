from pwn import *


print(cyclic(50))
print(shellcraft.sh())
print(hexdump(asm(shellcraft.sh())))


#local process interaction
p = process("/bin/sh")
p.sendline("echo hellow")
p.interactive()

#remote

r = remote("127.0.0.1",2222)
r.sendline("hellow")
r.interactive()
r.close()
