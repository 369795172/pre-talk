# Working - pre-talk changelog

## Changelog

### 2026-11-22（深夜）· 定锚态对齐（设备端 D11 落地后的一次性收口）

- 「听懂对方」v0.1.10 会前定锚落地后，README / rfc C3 / SKILL / test 四处一次性对齐成真实操作口径：待机长按（或镜腿手势键）进入锚采集 → 念开场白停顿定锚（「已定锚」指示）→ 逐结算注入 → 再长按清除；同时消除上一轮遗留的三处旧口播口径（review 第二轮点名）。
- rfc C3 保留教训存档：初版「口播即注入」与设备端单轮会话制不符，正确通道是设备侧定锚态。

### 2026-11-22（晚）· 外部 review 修复轮

- 修正 README/rfc 中「口播 60 字开场白即可锚定听懂对方」的失真表述：听懂对方（Rokid Agent Store 版）为单轮会话制（结算即销毁上下文），不存在会前注入面；开场白重新定位为「开口前自我锚定 + 未来设备支持会前定锚时的导出物」。
- `scaffold.py check --strict` 6 项 FAIL 清零：AGENTS.md 补 Scope / What NOT to do 节，working.md 补 Changelog / Lessons Learned 节名，prd.md 节名对齐 Non-Goals / Success Criteria。
- `check_card.sh` 支持透传参数（原先忽略命令行参数）；AGENTS.md 示例路径修正（向上汇报_功能延期通报.md）。

### 2026-11-22

- v0.1.0 首版：四步备谈工作流（登记/核心句筛除/排序卡/对方三问）+ 备谈卡模板 + 两张虚构示例卡 + 结构校验脚本（check_card.py/sh）。
- 定名 pre-talk（中文名：想清楚），与 Rokid 眼镜智能体「听懂对方」成对，slogan：先想清楚，再听懂对方。
- 决策否案落 docs/rfc.md（C1-C5）。

## Lessons Learned

- 给脑子的程序，不给嘴巴的句式。任何「改进表达」的产出物先过这一条再出门（源自黄执中《表达学院》公开课：只改口头用语的训练必失败，嘴巴迁就脑子）。
- 对外宣称的设备联动机制必须先读设备端代码再落笔：一句「平台 LLM 会把它当上文」的想象，在单轮会话制的真机面前就是虚假宣传（2026-11-22 外部 review 抓出）。
