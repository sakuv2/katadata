# coding:utf-8
import pandas as pd


class Kata:
    """[class]
    kataminoの問題データのくらす
    """

    def __init__(self, name, minos, rang):
        self.name = name  # 問題の名前(string)
        self.range = rang  # 問題の範囲[6-7](list of int)
        self.minos = minos  # ミノの配列(list of int)

    def __str__(self):
        a = self
        s = "<name:{}, range:{}, minos:{}>".format(a.name, a.range, a.minos)
        return s


def load(p):
    """[function]
    p: (int) ページ番号
    """
    df = pd.read_csv('data/p{}.csv'.format(p), header=None)
    return df.as_matrix().tolist()


class Katas:
    """[class]
    """

    def __init__(self):
        self.data = []
        self._i = 0

    def __str__(self):
        s = ""
        N = 3 if len(self) > 3 else len(self)
        for i in range(N):
            a = self.data[i]
            s += "<name:{}, range:{}, minos:{}>,\n".format(
                a.name, a.range, a.minos)
        if len(self) >= 3:
            s += "...\n"
            a = self.data[-1]
            s += "<name:{}, range:{}, minos:{}>".format(
                a.name, a.range, a.minos)
        else:
            s = s[:-2]
        return s

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i == len(self):
            raise StopIteration()
        value = self.data[self._i]
        self._i += 1
        return value

    def initialize(self, katas):
        k = Katas()
        k.data = katas
        return k

    def load_all(self):
        """[function]
        全部読み込む
        """
        katas = Katas()

        # p4
        for i in range(7):
            dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
            k = Kata("4-{}".format(dic[i]), load(4)[i], rang=[3, 8])
            katas.append(k)

        # p5
        for i in range(7):
            dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
            k = Kata("5-{}".format(dic[i]), load(5)[i], rang=[5, 9])
            katas.append(k)

        # p6
        for i in range(7):
            dic = ['H', 'I', 'J', 'K', 'L', 'M', 'N']
            k = Kata("6-{}".format(dic[i]), load(6)[i], rang=[5, 9])
            katas.append(k)

        # p7
        for i in range(8):
            dic = ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
            k = Kata("7-{}".format(dic[i]), load(7)[i], rang=[6, 8])
            katas.append(k)

        # p8
        for i in range(7):
            dic = ['W', 'X', 'Y', 'Z', '♥', '♦', '♠', '♣']
            k = Kata("8-{}".format(dic[i]), load(8)[i], rang=[6, 8])
            katas.append(k)

        # p9
        for i in range(12):
            dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
            k = Kata("9-{}".format(dic[i]), load(9)[i], rang=[4, 11])
            katas.append(k)

        # p10
        for i in range(12):
            dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
            k = Kata("10-{}".format(dic[i]), load(10)[i], rang=[5, 11])
            katas.append(k)

        # p11
        for i in range(10):
            dic = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10']
            k = Kata("11-{}".format(dic[i]), load(11)[i], rang=[7, 10])
            katas.append(k)

        # p12
        for i in range(10):
            dic = ['N11', 'N12', 'N13', 'N14', 'N15',
                   'N16', 'N17', 'N18', 'N19', 'N20']
            k = Kata("12-{}".format(dic[i]), load(12)[i], rang=[7, 10])
            katas.append(k)

        # p13
        for i in range(10):
            dic = ['N21', 'N22', 'N23', 'N24', 'N25',
                   'N26', 'N27', 'N28', 'N29', 'N30']
            k = Kata("13-{}".format(dic[i]), load(13)[i], rang=[7, 10])
            katas.append(k)

        # p14
        for i in range(10):
            dic = ['N31', 'N32', 'N33', 'N34', 'N35',
                   'N36', 'N37', 'N38', 'N39', 'N40']
            k = Kata("14-{}".format(dic[i]), load(14)[i], rang=[7, 10])
            katas.append(k)
        self.data = katas.data[:]
        return katas

    def append(self, kata):
        self.data.append(kata)

    def find_name(self, name):
        """[function]
        名前と一致するKataクラスデータを1つ返す
        return: {Kata}
        """
        a = [x for x in self.data if x.name == name]
        if len(a) > 0:
            print("a")
            return a[0]
        else:
            return a

    def find_len(self, m):
        """[function]
        使用するミノ数と一致する問題を探す
        return: (Katas)
        """
        a = [x for x in self.data if x.range[0] <= m and x.range[1] >= m]
        return self.initialize(a)

    def find_minos(self, minos):
        """[function]
        一致する問題を探す
        minos: {list of int}
        return: {Katas}
        """
        m = len(minos)
        a = self.find_len(m).data
        x = []
        for b in a:
            c = b.minos[:m]
            if sorted(c) == sorted(minos):
                x.append(b)
        return self.initialize(x)

    def find_rminos(self, minos):
        """[function]
        minosの補集合を探索する
        minos: {list of int}
        return: {Katas}
        """
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for i in minos:
            a.remove(i)
        return self.find_minos(a)
