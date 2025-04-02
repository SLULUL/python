import numpy as np

s = input("请输入八名裁判的打分，以“,”分隔：")
scores = [float(x) for x in s.split(",")]

if len(scores) != 8:
    print("请输入8个有效分数！")
else:
    scores.remove(max(scores))
    scores.remove(min(scores))
    # scores.remove(np.max(scores))
    # scores.remove(np.min(scores))
    avg = np.average(scores)
    print(f"最终得分：{avg:.2f}")
