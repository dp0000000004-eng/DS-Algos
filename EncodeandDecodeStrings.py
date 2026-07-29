class Encrypt:
    def encoding(self, chat:list[str] ) -> str:

        s = ""

        for word in chat:
            if word == "":
                s += "_"
            for i, w in enumerate(word):
                if i == len(word) - 1:
                    s += w + "`"
                else:
                    s += w


        return s

    def decoding(self, s:str) -> list[str]:

        store = ""
        f_ans = []

        for i in s:
            if i == "`":
                f_ans.append(store)
                store = ""
            elif i == "_":
                f_ans.append("")
            else:
                store += i

        if store != "":
            f_ans.append(store)

        return f_ans


chat = ["Hy", " How Are You", "Is everything ok ?"]


func = Encrypt()
sender = func.encoding(chat)
print(sender)
resiver = func.decoding(sender)
print(resiver)