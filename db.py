import sqlite3
from xmlrpc.client import boolean

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def mainID(self, userID):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `question` WHERE `user_id` = ? ORDER BY `id` DESC", (userID, )).fetchone()
        return result[0]

    # def get_region(self, idRegion):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT * FROM `area` WHERE `nomer` = ?", (idRegion,)).fetchone()
    #     return result

    def insert_user(self, user_id, fio):
        with self.connection:
            result = self.cursor.execute("INSERT INTO `question` (`user_id`) VALUES (?)", (user_id, )).fetchone()
        return result

    def userFioExists(self, userID):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `question` WHERE `user_id` = ? ORDER BY `id` DESC", (userID,)).fetchone()
        return result[4]

    def update_user(self, userID, fio):
        with self.connection:
            mainid = self.mainID(userID)
            result = self.cursor.execute("UPDATE `question` SET `fio` = ? WHERE `id` = ?", (fio, mainid)).fetchone()
        return result

    def get_ans(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `question` WHERE `user_id` = ? ORDER BY `id` DESC", (user_id,)).fetchone()
        return result

    def updateCat(self, cat, userID):
        with self.connection:
            mainid = self.mainID(userID)
            result = self.cursor.execute("UPDATE `question` SET `cat` = ? WHERE `id` = ?", (cat, mainid)).fetchone()
        return result

    def setQuestion(self, userID, question):
        with self.connection:
            mainid = self.mainID(userID)
            result = self.cursor.execute("UPDATE `question` SET `question` = ? WHERE `id` = ?", (question, mainid, )).fetchone()
        return result

    def selectedCat(self, userID):
        with self.connection:
            mainid = self.mainID(userID)
            result = self.cursor.execute("SELECT * FROM `question` WHERE `id` = ? ORDER BY `id` DESC", (mainid, )).fetchone()
        return result

    def getLastQuest(self, userID):
        with self.connection:
            mainid = self.mainID(userID)
            result = self.cursor.execute("SELECT * FROM `question` WHERE `id` = ? ORDER BY `id` DESC", (mainid, )).fetchone()
        return result[2]

    def setLang(self, userID, lang):
        with self.connection:
            mainid = self.mainID(userID)
            result = self.cursor.execute("UPDATE `question` SET `lang` = ? WHERE `id` = ?", (lang, mainid, )).fetchone()
        return result

    def getLang(self, userID):
        with self.connection:
            mainid = self.mainID(userID)
            result = self.cursor.execute("SELECT * FROM `question` WHERE `id` = ? ORDER BY `id` DESC", (mainid, )).fetchone()
        return result[5]

    def getUser(self, userID):
        with self.connection:
            mainid = self.mainID(userID)
            result = self.cursor.execute("SELECT * FROM `question` WHERE `id` = ? ORDER BY `id` DESC", (mainid, )).fetchone()
        return result[4]