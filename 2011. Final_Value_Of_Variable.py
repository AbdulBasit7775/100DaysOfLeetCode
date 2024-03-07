def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0;
        for operation in range(len(operations)):
            if operations[operation] == '--X' or operations[operation] == 'X--':
                X -= 1
            else:
                X += 1 
        return X