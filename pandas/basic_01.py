# pandas 2.2.3

# 介绍 pandas 的基础用法

import pandas as pd

def main():
    # ========== 读取数据 获取信息 ==========
    df = pd.read_csv("data.csv")
    # 输出整张表 表是 2D 的数据
    # print(df)

    # 将 Name 列的数据类型转换为字符串
    df['Name'] = df['Name'].astype(str) # 后面可以填入哪些类型呢？

    # 输出前 3 行
    # print(df.head(3))

    # 获取表的部分列
    name_score = df[["Name", "Score"]]
    # print(name_score)

    # 输出每一列的名称和类型，可能的类型有：int64, float64, object
    # object 表示 Python 对象，比如字符串 OR 混合类型
    # string 类型 pandas 也会显示为 object
    print(df.dtypes)

    # 输出表的大小
    columns_size, rows_size = df.shape
    print(f"columns_size: {columns_size}, rows_size: {rows_size}")

    # 输出表的列名 以 column 为单位
    # print(df.columns)

    # 输出表的索引 以 row 为单位
    # print(df.index)

    # 一张表（CSV 读入的 DataFrame）是 2D 的，可以理解为 2D 的数组
    # 从 2D 的数据中，提取出 1D 的数据（Series）
    # 提取出某一列 输出所有人的名字
    # print(df["Name"])

    # Series 是 1D 的数据，一般表示一列，但是也可以表示一行
    # 创建一个行 Series
    row_series = pd.Series({'A': 1, 'B': 2, 'C': 3}, name=0)
    # print(row_series)
    # 输出：
    # A    1
    # B    2
    # C    3
    # Name: 0, dtype: int64

    # 提取出某一行的数据 输出第 0 行（第一个人的所有信息）
    # print(df.loc[0])

    # ========== 数据筛选 ==========
    # 筛选数据呢，一般我们都是筛选行（哪几行满足条件）

    # 筛选出所有年龄大于 30 岁的人
    # 注意这个写法 df["Age"] > 30 返回的是一个布尔值的 Series
    # 布尔值的 Series 可以作为索引，筛选出满足条件的行
    # print(df[df["Age"] > 30])

    # 找到成绩最高的人 输出恭喜他的信息
    highest_score = df['Score'].max()
    highest_score_name = df.loc[df['Score'].idxmax(), 'Name']
    print(f"Congratulations to {highest_score_name} ({highest_score})!")

    # ========== 数据修改 ==========
    # 手动添加几个新人
    new_person = pd.DataFrame({
        "Name": ["John Doe", "Jane Smith", "Alice Johnson"],
        "Age": [25, 30, 28],
        "Score": [95, None, None], # 这里 None 表示缺失值 所有 list 的长度必须一致
        "Gender": ["M", "F", "F"] # 这里 column 的顺序可以不一致
    })
    # 将新的人添加到表的末尾
    # 注意：ignore_index=True 表示重新索引 也就是后面的表的索引会重新分配
    df = pd.concat([df, new_person], ignore_index=True)
    # print(df)

    # 将缺失的成绩值都填充为 60
    df['Score'] = df['Score'].fillna(60)
    # print(df)

    # 将成绩除以最高分 得到一个 0-1 之间的数 保存在一个新列中
    df['Score_Rate'] = df['Score'] / df['Score'].max()

    # 增加一列 表示每个人的名字缩写
    def name_abbreviation(name):
        # 找到所有大写字母
        return ''.join([char for char in name if char.isupper()])
    df['Name_Abbreviation'] = df['Name'].apply(name_abbreviation)
    # print(df)

    # 增加一列 表示每个人的原始索引
    # 数据长度不一定一致 不足的部分填充 NaN
    origin_index = pd.Series([1, 2, 3], name = "origin_index").astype("int64")
    # 将 origin_index 补充到 df 的长度，空的值用 0 填充，默认的 Nan 是 float64 类型
    origin_index = origin_index.reindex(df.index, fill_value=0)
    # axis=1 表示按列拼接（水平） axis=0 表示按行拼接（垂直）
    df = pd.concat([df, origin_index], axis=1)

    # 按照成绩排序 从高到低 当成绩相同时，按照年龄排序 从低到高
    # 注意排序不会重新分配索引
    df = df.sort_values(by=["Score", "Age"], ascending=[False, True])
    # 将排序后的表输出
    # print(df)
    # 将排序后的表的索引重新分配
    df = df.reset_index(drop=True)
    print(df)

    # ========== 数据保存 ==========
    # 将表保存为 CSV 文件
    # 注意：index=False 表示不保存索引
    # df.to_csv("output.csv", index=False)

if __name__ == "__main__":
    main()
