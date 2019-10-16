# 将  λ 修改为 $



```lua

-- cmder\vendor\clink.lua文件中第51行中{lamb}修改为$

-- 修改前
local cmder_prompt = "\x1b[1;32;40m{cwd} {git}{hg}{svn} \n\x1b[1;39;40m{lamb} \x1b[0m"

-- 修改后
local cmder_prompt = "\x1b[1;32;40m{cwd} {git}{hg}{svn} \n\x1b[1;39;40m$ \x1b[0m"

```

