def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        number_of_employee = 0
        for employee_work in hours:
            if employee_work >= target:
                number_of_employee += 1
        return number_of_employee