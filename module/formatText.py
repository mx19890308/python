class formatText(object):

    def __init__(self, filePath, fileSplitStr="#",headerStr="=", lineStr="-", splitStr="+", splitStr2 = "|"):
        self.__content = []
        self.__columns_len = []
        self.__headerStr = headerStr
        self.__lineStr = lineStr
        self.__splitStr = splitStr
        self.__splitStr2 = splitStr2
        self.__init_data(filePath, fileSplitStr)

    def __init_data(self, filePath, fileSplitStr):
        with open(filePath) as op:
            for line in op:
                column = line.strip().split(fileSplitStr)
                self.__content.append(column)
                self.__compare_len(column)

    def __compare_len(self, column):
        colLen = len(column)
        for index in range(0, colLen):
            if len(self.__columns_len) < index + 1:
                self.__columns_len.append(0)
            if self.__columns_len[index] < len(column[index]):
                self.__columns_len[index] = len(column[index])

    def __repeat(self, rStr, times):
       return "".join([rStr for i in range(0, times)])

    def __splitLine(self, lineStr):
        final = ""
        for column in self.__columns_len:
            final += "%s%s" % (self.__splitStr, self.__repeat(lineStr, column + 1))
        return final + self.__splitStr

    def __lineFormat(self):
        content = self.__splitStr2.join(["% %-%ds " % i for i in self.__columns_len])
        return "%s%s%s" % (self.__splitStr2, content, self.__splitStr2)

    def output(self):
        totalLen = sum(self.__columns_len) + len(self.__columns_len) * 2 + 1
        formatStr = self.__lineFormat()
        splitLineStr = self.__splitLine(self.__lineStr)
        headerUpStr = self.__repeat(self.__headerStr, totalLen)
        headerDownStr = self.__splitLine(self.__headerStr)

        for i in range(0, len(self.__content)):
            if i == 0: print(headerUpStr)
            print(formatStr % tuple(self.__content[i]))
            outputStr = headerDownStr if i == 0 else splitLineStr
            print(outputStr)
        print(self.__columns_len)


formatText("src.txt", "#").output()
