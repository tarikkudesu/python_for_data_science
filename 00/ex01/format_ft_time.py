from datetime import datetime

now = datetime.now();
epoc = datetime.fromtimestamp(0).strftime("%B %d, %Y:");
print(f"Seconds since {epoc} {now.timestamp():,} or {now.timestamp():.2e} in scientific notation")
print(now.strftime("%b %d %Y"))
