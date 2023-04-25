import re


def valida_cpf(cpf):
    """
        Efetua a validação do CPF, tanto formatação quanto dígito verificadores.
        Args:
            cpf (str): CPF a ser validado
        Returns:
            bool:
                - False, quando o CPF não possuir o formato 999.999.999-99;
                - False, quando o CPF não possuir 11 caracteres numéricos;
                - False, quando os dígitos verificadores forem inválidos;
                - True, caso contrário.
        Examples:
        >>> valida_cpf('529.982.247-25')
        True
        >>> valida_cpf('52998224725')
        False
        >>> valida_cpf('111.111.111-11')
        False
        """

    # Verifica a formatação do CPF utilizando expressão regular
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True
