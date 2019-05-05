# linux-kernel-entropy-logger
Slightly modify the Linux kernel to output the entropy source information using printk. User space program can retrieve this information using dmesg. 

This is based on linux-4.14.102. See https://www.cyberciti.biz/tips/compiling-linux-kernel-26.html for Linux kernel build instructions. 

1. edits to drivers/char/random.c are inside the add_timer_randomness function. 

2. in the config file, the CONFIG_LOG_BUF_SHIFT is set to 25 to make the kernel ring buffer size 32MB. 

3. log-10w.txt is dumped using "dmesg >> log-10w.txt".

4. convert.py converts it to a format that can be processed by the neural network. convert-new.py processes slightly different inputs. 
