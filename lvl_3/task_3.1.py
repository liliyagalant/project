# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[None for j in range(cols)] for i in range(rows)]
    
    def set_value(self, row, col, value):
        if row < self.rows and col < self.cols:
            self.matrix[row][col] = value
            return True
        return False
    
    def replace_value(self, row, col, value):
        if row < self.rows and col < self.cols:
            if self.matrix[row][col]:
                self.matrix[row][col] = value
                return True
        return False
    
    def get_num_rows(self):
        return self.rows
    
    def get_num_cols(self):
        return self.cols
    
    def __str__(self):
        return '\n'.join([' '.join(['{}'.format(elem) if elem else '' for elem in row]) for row in self.matrix])
matr = Matrix(10, 10)
print(matr)
matr.set_value(5, 6, 3)
matr.replace_value(5, 6, 10)
print(matr)
