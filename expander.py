
def expandOffsuit(card1):
    rangeoff = []
    if "AK" in card1:
        rangeoff.append("AsKh")
        rangeoff.append("AsKd")
        rangeoff.append("AsKc")

        rangeoff.append("AhKs")
        rangeoff.append("AhKd")
        rangeoff.append("AhKc")

        rangeoff.append("AdKs")
        rangeoff.append("AdKh")
        rangeoff.append("AdKc")

        rangeoff.append("AcKs")
        rangeoff.append("AcKh")
        rangeoff.append("AcKd")
    elif "AQ" in card1:
        rangeoff.append("AsQh")
        rangeoff.append("AsQd")
        rangeoff.append("AsQc")

        rangeoff.append("AhQs")
        rangeoff.append("AhQd")
        rangeoff.append("AhQc")

        rangeoff.append("AdQs")
        rangeoff.append("AdQh")
        rangeoff.append("AdQc")

        rangeoff.append("AcQs")
        rangeoff.append("AcQh")
        rangeoff.append("AcQd")
    elif "AJ" in card1:
        rangeoff.append("AsJh")
        rangeoff.append("AsJd")
        rangeoff.append("AsJc")

        rangeoff.append("AhJs")
        rangeoff.append("AhJd")
        rangeoff.append("AhJc")

        rangeoff.append("AdJs")
        rangeoff.append("AdJh")
        rangeoff.append("AdJc")

        rangeoff.append("AcJs")
        rangeoff.append("AcJh")
        rangeoff.append("AcJd")
    elif "AT" in card1:
        rangeoff.append("AsTh")
        rangeoff.append("AsTd")
        rangeoff.append("AsTc")

        rangeoff.append("AhTs")
        rangeoff.append("AhTd")
        rangeoff.append("AhTc")

        rangeoff.append("AdTs")
        rangeoff.append("AdTh")
        rangeoff.append("AdTc")

        rangeoff.append("AcTs")
        rangeoff.append("AcTh")
        rangeoff.append("AcTd")
    elif "A9" in card1:
        rangeoff.append("As9h")
        rangeoff.append("As9d")
        rangeoff.append("As9c")

        rangeoff.append("Ah9s")
        rangeoff.append("Ah9d")
        rangeoff.append("Ah9c")

        rangeoff.append("Ad9s")
        rangeoff.append("Ad9h")
        rangeoff.append("Ad9c")

        rangeoff.append("Ac9s")
        rangeoff.append("Ac9h")
        rangeoff.append("Ac9d")
    elif "A8" in card1:
        rangeoff.append("As8h")
        rangeoff.append("As8d")
        rangeoff.append("As8c")

        rangeoff.append("Ah8s")
        rangeoff.append("Ah8d")
        rangeoff.append("Ah8c")

        rangeoff.append("Ad8s")
        rangeoff.append("Ad8h")
        rangeoff.append("Ad8c")

        rangeoff.append("Ac8s")
        rangeoff.append("Ac8h")
        rangeoff.append("Ac8d")
    elif "A7" in card1:
        rangeoff.append("As7h")
        rangeoff.append("As7d")
        rangeoff.append("As7c")

        rangeoff.append("Ah7s")
        rangeoff.append("Ah7d")
        rangeoff.append("Ah7c")

        rangeoff.append("Ad7s")
        rangeoff.append("Ad7h")
        rangeoff.append("Ad7c")

        rangeoff.append("Ac7s")
        rangeoff.append("Ac7h")
        rangeoff.append("Ac7d")
    elif "A6" in card1:
        rangeoff.append("As6h")
        rangeoff.append("As6d")
        rangeoff.append("As6c")

        rangeoff.append("Ah6s")
        rangeoff.append("Ah6d")
        rangeoff.append("Ah6c")

        rangeoff.append("Ad6s")
        rangeoff.append("Ad6h")
        rangeoff.append("Ad6c")

        rangeoff.append("Ac6s")
        rangeoff.append("Ac6h")
        rangeoff.append("Ac6d")
    elif "A5" in card1:
        rangeoff.append("As5h")
        rangeoff.append("As5d")
        rangeoff.append("As5c")

        rangeoff.append("Ah5s")
        rangeoff.append("Ah5d")
        rangeoff.append("Ah5c")

        rangeoff.append("Ad5s")
        rangeoff.append("Ad5h")
        rangeoff.append("Ad5c")

        rangeoff.append("Ac5s")
        rangeoff.append("Ac5h")
        rangeoff.append("Ac5d")
    elif "A4" in card1:
        rangeoff.append("As4h")
        rangeoff.append("As4d")
        rangeoff.append("As4c")

        rangeoff.append("Ah4s")
        rangeoff.append("Ah4d")
        rangeoff.append("Ah4c")

        rangeoff.append("Ad4s")
        rangeoff.append("Ad4h")
        rangeoff.append("Ad4c")

        rangeoff.append("Ac4s")
        rangeoff.append("Ac4h")
        rangeoff.append("Ac4d")
    elif "A3" in card1:
        rangeoff.append("As3h")
        rangeoff.append("As3d")
        rangeoff.append("As3c")

        rangeoff.append("Ah3s")
        rangeoff.append("Ah3d")
        rangeoff.append("Ah3c")

        rangeoff.append("Ad3s")
        rangeoff.append("Ad3h")
        rangeoff.append("Ad3c")

        rangeoff.append("Ac3s")
        rangeoff.append("Ac3h")
        rangeoff.append("Ac3d")
    elif "A2" in card1:
        rangeoff.append("As2h")
        rangeoff.append("As2d")
        rangeoff.append("As2c")

        rangeoff.append("Ah2s")
        rangeoff.append("Ah2d")
        rangeoff.append("Ah2c")

        rangeoff.append("Ad2s")
        rangeoff.append("Ad2h")
        rangeoff.append("Ad2c")

        rangeoff.append("Ac2s")
        rangeoff.append("Ac2h")
        rangeoff.append("Ac2d")
    elif "KQ" in card1:
        rangeoff.append("KsQh")
        rangeoff.append("KsQd")
        rangeoff.append("KsQc")

        rangeoff.append("KhQs")
        rangeoff.append("KhQd")
        rangeoff.append("KhQc")

        rangeoff.append("KdQs")
        rangeoff.append("KdQh")
        rangeoff.append("KdQc")

        rangeoff.append("KcQs")
        rangeoff.append("KcQh")
        rangeoff.append("KcQd")
    elif "KJ" in card1:
        rangeoff.append("KsJh")
        rangeoff.append("KsJd")
        rangeoff.append("KsJc")

        rangeoff.append("KhJs")
        rangeoff.append("KhJd")
        rangeoff.append("KhJc")

        rangeoff.append("KdJs")
        rangeoff.append("KdJh")
        rangeoff.append("KdJc")

        rangeoff.append("KcJs")
        rangeoff.append("KcJh")
        rangeoff.append("KcJd")
    elif "KT" in card1:
        rangeoff.append("KsTh")
        rangeoff.append("KsTd")
        rangeoff.append("KsTc")

        rangeoff.append("KhTs")
        rangeoff.append("KhTd")
        rangeoff.append("KhTc")

        rangeoff.append("KdTs")
        rangeoff.append("KdTh")
        rangeoff.append("KdTc")

        rangeoff.append("KcTs")
        rangeoff.append("KcTh")
        rangeoff.append("KcTd")
    elif "K9" in card1:
        rangeoff.append("Ks9h")
        rangeoff.append("Ks9d")
        rangeoff.append("Ks9c")

        rangeoff.append("Kh9s")
        rangeoff.append("Kh9d")
        rangeoff.append("Kh9c")

        rangeoff.append("Kd9s")
        rangeoff.append("Kd9h")
        rangeoff.append("Kd9c")

        rangeoff.append("Kc9s")
        rangeoff.append("Kc9h")
        rangeoff.append("Kc9d")
    elif "K8" in card1:
        rangeoff.append("Ks8h")
        rangeoff.append("Ks8d")
        rangeoff.append("Ks8c")

        rangeoff.append("Kh8s")
        rangeoff.append("Kh8d")
        rangeoff.append("Kh8c")

        rangeoff.append("Kd8s")
        rangeoff.append("Kd8h")
        rangeoff.append("Kd8c")

        rangeoff.append("Kc8s")
        rangeoff.append("Kc8h")
        rangeoff.append("Kc8d")
    elif "K7" in card1:
        rangeoff.append("Ks7h")
        rangeoff.append("Ks7d")
        rangeoff.append("Ks7c")

        rangeoff.append("Kh7s")
        rangeoff.append("Kh7d")
        rangeoff.append("Kh7c")

        rangeoff.append("Kd7s")
        rangeoff.append("Kd7h")
        rangeoff.append("Kd7c")

        rangeoff.append("Kc7s")
        rangeoff.append("Kc7h")
        rangeoff.append("Kc7d")
    elif "K6" in card1:
        rangeoff.append("Ks6h")
        rangeoff.append("Ks6d")
        rangeoff.append("Ks6c")

        rangeoff.append("Kh6s")
        rangeoff.append("Kh6d")
        rangeoff.append("Kh6c")

        rangeoff.append("Kd6s")
        rangeoff.append("Kd6h")
        rangeoff.append("Kd6c")

        rangeoff.append("Kc6s")
        rangeoff.append("Kc6h")
        rangeoff.append("Kc6d")
    elif "K5" in card1:
        rangeoff.append("Ks5h")
        rangeoff.append("Ks5d")
        rangeoff.append("Ks5c")

        rangeoff.append("Kh5s")
        rangeoff.append("Kh5d")
        rangeoff.append("Kh5c")

        rangeoff.append("Kd5s")
        rangeoff.append("Kd5h")
        rangeoff.append("Kd5c")

        rangeoff.append("Kc5s")
        rangeoff.append("Kc5h")
        rangeoff.append("Kc5d")
    elif "K4" in card1:
        rangeoff.append("Ks4h")
        rangeoff.append("Ks4d")
        rangeoff.append("Ks4c")

        rangeoff.append("Kh4s")
        rangeoff.append("Kh4d")
        rangeoff.append("Kh4c")

        rangeoff.append("Kd4s")
        rangeoff.append("Kd4h")
        rangeoff.append("Kd4c")

        rangeoff.append("Kc4s")
        rangeoff.append("Kc4h")
        rangeoff.append("Kc4d")
    elif "K3" in card1:
        rangeoff.append("Ks3h")
        rangeoff.append("Ks3d")
        rangeoff.append("Ks3c")

        rangeoff.append("Kh3s")
        rangeoff.append("Kh3d")
        rangeoff.append("Kh3c")

        rangeoff.append("Kd3s")
        rangeoff.append("Kd3h")
        rangeoff.append("Kd3c")

        rangeoff.append("Kc3s")
        rangeoff.append("Kc3h")
        rangeoff.append("Kc3d")
    elif "K2" in card1:
        rangeoff.append("Ks2h")
        rangeoff.append("Ks2d")
        rangeoff.append("Ks2c")

        rangeoff.append("Kh2s")
        rangeoff.append("Kh2d")
        rangeoff.append("Kh2c")

        rangeoff.append("Kd2s")
        rangeoff.append("Kd2h")
        rangeoff.append("Kd2c")

        rangeoff.append("Kc2s")
        rangeoff.append("Kc2h")
        rangeoff.append("Kc2d")
    elif "QJ" in card1:
        rangeoff.append("QsJh")
        rangeoff.append("QsJd")
        rangeoff.append("QsJc")

        rangeoff.append("QhJs")
        rangeoff.append("QhJd")
        rangeoff.append("QhJc")

        rangeoff.append("QdJs")
        rangeoff.append("QdJh")
        rangeoff.append("QdJc")

        rangeoff.append("QcJs")
        rangeoff.append("QcJh")
        rangeoff.append("QcJd")
    elif "QT" in card1:
        rangeoff.append("QsTh")
        rangeoff.append("QsTd")
        rangeoff.append("QsTc")

        rangeoff.append("QhTs")
        rangeoff.append("QhTd")
        rangeoff.append("QhTc")

        rangeoff.append("QdTs")
        rangeoff.append("QdTh")
        rangeoff.append("QdTc")

        rangeoff.append("QcTs")
        rangeoff.append("QcTh")
        rangeoff.append("QcTd")
    elif "Q9" in card1:
        rangeoff.append("Qs9h")
        rangeoff.append("Qs9d")
        rangeoff.append("Qs9c")

        rangeoff.append("Qh9s")
        rangeoff.append("Qh9d")
        rangeoff.append("Qh9c")

        rangeoff.append("Qd9s")
        rangeoff.append("Qd9h")
        rangeoff.append("Qd9c")

        rangeoff.append("Qc9s")
        rangeoff.append("Qc9h")
        rangeoff.append("Qc9d")
    elif "Q8" in card1:
        rangeoff.append("Qs8h")
        rangeoff.append("Qs8d")
        rangeoff.append("Qs8c")

        rangeoff.append("Qh8s")
        rangeoff.append("Qh8d")
        rangeoff.append("Qh8c")

        rangeoff.append("Qd8s")
        rangeoff.append("Qd8h")
        rangeoff.append("Qd8c")

        rangeoff.append("Qc8s")
        rangeoff.append("Qc8h")
        rangeoff.append("Qc8d")
    elif "Q7" in card1:
        rangeoff.append("Qs7h")
        rangeoff.append("Qs7d")
        rangeoff.append("Qs7c")

        rangeoff.append("Qh7s")
        rangeoff.append("Qh7d")
        rangeoff.append("Qh7c")

        rangeoff.append("Qd7s")
        rangeoff.append("Qd7h")
        rangeoff.append("Qd7c")

        rangeoff.append("Qc7s")
        rangeoff.append("Qc7h")
        rangeoff.append("Qc7d")
    elif "Q6" in card1:
        rangeoff.append("Qs6h")
        rangeoff.append("Qs6d")
        rangeoff.append("Qs6c")

        rangeoff.append("Qh6s")
        rangeoff.append("Qh6d")
        rangeoff.append("Qh6c")

        rangeoff.append("Qd6s")
        rangeoff.append("Qd6h")
        rangeoff.append("Qd6c")

        rangeoff.append("Qc6s")
        rangeoff.append("Qc6h")
        rangeoff.append("Qc6d")
    elif "Q5" in card1:
        rangeoff.append("Qs5h")
        rangeoff.append("Qs5d")
        rangeoff.append("Qs5c")

        rangeoff.append("Qh5s")
        rangeoff.append("Qh5d")
        rangeoff.append("Qh5c")

        rangeoff.append("Qd5s")
        rangeoff.append("Qd5h")
        rangeoff.append("Qd5c")

        rangeoff.append("Qc5s")
        rangeoff.append("Qc5h")
        rangeoff.append("Qc5d")
    elif "Q4" in card1:
        rangeoff.append("Qs4h")
        rangeoff.append("Qs4d")
        rangeoff.append("Qs4c")

        rangeoff.append("Qh4s")
        rangeoff.append("Qh4d")
        rangeoff.append("Qh4c")

        rangeoff.append("Qd4s")
        rangeoff.append("Qd4h")
        rangeoff.append("Qd4c")

        rangeoff.append("Qc4s")
        rangeoff.append("Qc4h")
        rangeoff.append("Qc4d")
    elif "Q3" in card1:
        rangeoff.append("Qs3h")
        rangeoff.append("Qs3d")
        rangeoff.append("Qs3c")

        rangeoff.append("Qh3s")
        rangeoff.append("Qh3d")
        rangeoff.append("Qh3c")

        rangeoff.append("Qd3s")
        rangeoff.append("Qd3h")
        rangeoff.append("Qd3c")

        rangeoff.append("Qc3s")
        rangeoff.append("Qc3h")
        rangeoff.append("Qc3d")
    elif "Q2" in card1:
        rangeoff.append("Qs2h")
        rangeoff.append("Qs2d")
        rangeoff.append("Qs2c")

        rangeoff.append("Qh2s")
        rangeoff.append("Qh2d")
        rangeoff.append("Qh2c")

        rangeoff.append("Qd2s")
        rangeoff.append("Qd2h")
        rangeoff.append("Qd2c")

        rangeoff.append("Qc2s")
        rangeoff.append("Qc2h")
        rangeoff.append("Qc2d")
    
    elif "JT" in card1:
        rangeoff.append("JsTh")
        rangeoff.append("JsTd")
        rangeoff.append("JsTc")

        rangeoff.append("JhTs")
        rangeoff.append("JhTd")
        rangeoff.append("JhTc")

        rangeoff.append("JdTs")
        rangeoff.append("JdTh")
        rangeoff.append("JdTc")

        rangeoff.append("JcTs")
        rangeoff.append("JcTh")
        rangeoff.append("JcTd")
    elif "J9" in card1:
        rangeoff.append("Js9h")
        rangeoff.append("Js9d")
        rangeoff.append("Js9c")

        rangeoff.append("Jh9s")
        rangeoff.append("Jh9d")
        rangeoff.append("Jh9c")

        rangeoff.append("Jd9s")
        rangeoff.append("Jd9h")
        rangeoff.append("Jd9c")

        rangeoff.append("Jc9s")
        rangeoff.append("Jc9h")
        rangeoff.append("Jc9d")
    elif "J8" in card1:
        rangeoff.append("Js8h")
        rangeoff.append("Js8d")
        rangeoff.append("Js8c")

        rangeoff.append("Jh8s")
        rangeoff.append("Jh8d")
        rangeoff.append("Jh8c")

        rangeoff.append("Jd8s")
        rangeoff.append("Jd8h")
        rangeoff.append("Jd8c")

        rangeoff.append("Jc8s")
        rangeoff.append("Jc8h")
        rangeoff.append("Jc8d")
    elif "J7" in card1:
        rangeoff.append("Js7h")
        rangeoff.append("Js7d")
        rangeoff.append("Js7c")

        rangeoff.append("Jh7s")
        rangeoff.append("Jh7d")
        rangeoff.append("Jh7c")

        rangeoff.append("Jd7s")
        rangeoff.append("Jd7h")
        rangeoff.append("Jd7c")

        rangeoff.append("Jc7s")
        rangeoff.append("Jc7h")
        rangeoff.append("Jc7d")
    elif "J6" in card1:
        rangeoff.append("Js6h")
        rangeoff.append("Js6d")
        rangeoff.append("Js6c")

        rangeoff.append("Jh6s")
        rangeoff.append("Jh6d")
        rangeoff.append("Jh6c")

        rangeoff.append("Jd6s")
        rangeoff.append("Jd6h")
        rangeoff.append("Jd6c")

        rangeoff.append("Jc6s")
        rangeoff.append("Jc6h")
        rangeoff.append("Jc6d")
    elif "J5" in card1:
        rangeoff.append("Js5h")
        rangeoff.append("Js5d")
        rangeoff.append("Js5c")

        rangeoff.append("Jh5s")
        rangeoff.append("Jh5d")
        rangeoff.append("Jh5c")

        rangeoff.append("Jd5s")
        rangeoff.append("Jd5h")
        rangeoff.append("Jd5c")

        rangeoff.append("Jc5s")
        rangeoff.append("Jc5h")
        rangeoff.append("Jc5d")
    elif "J4" in card1:
        rangeoff.append("Js4h")
        rangeoff.append("Js4d")
        rangeoff.append("Js4c")

        rangeoff.append("Jh4s")
        rangeoff.append("Jh4d")
        rangeoff.append("Jh4c")

        rangeoff.append("Jd4s")
        rangeoff.append("Jd4h")
        rangeoff.append("Jd4c")

        rangeoff.append("Jc4s")
        rangeoff.append("Jc4h")
        rangeoff.append("Jc4d")
    elif "J3" in card1:
        rangeoff.append("Js3h")
        rangeoff.append("Js3d")
        rangeoff.append("Js3c")

        rangeoff.append("Jh3s")
        rangeoff.append("Jh3d")
        rangeoff.append("Jh3c")

        rangeoff.append("Jd3s")
        rangeoff.append("Jd3h")
        rangeoff.append("Jd3c")

        rangeoff.append("Jc3s")
        rangeoff.append("Jc3h")
        rangeoff.append("Jc3d")
    elif "J2" in card1:
        rangeoff.append("Js2h")
        rangeoff.append("Js2d")
        rangeoff.append("Js2c")

        rangeoff.append("Jh2s")
        rangeoff.append("Jh2d")
        rangeoff.append("Jh2c")

        rangeoff.append("Jd2s")
        rangeoff.append("Jd2h")
        rangeoff.append("Jd2c")

        rangeoff.append("Jc2s")
        rangeoff.append("Jc2h")
        rangeoff.append("Jc2d")
    elif "T9" in card1:
        rangeoff.append("Ts9h")
        rangeoff.append("Ts9d")
        rangeoff.append("Ts9c")

        rangeoff.append("Th9s")
        rangeoff.append("Th9d")
        rangeoff.append("Th9c")

        rangeoff.append("Td9s")
        rangeoff.append("Td9h")
        rangeoff.append("Td9c")

        rangeoff.append("Tc9s")
        rangeoff.append("Tc9h")
        rangeoff.append("Tc9d")
    elif "T8" in card1:
        rangeoff.append("Ts8h")
        rangeoff.append("Ts8d")
        rangeoff.append("Ts8c")

        rangeoff.append("Th8s")
        rangeoff.append("Th8d")
        rangeoff.append("Th8c")

        rangeoff.append("Td8s")
        rangeoff.append("Td8h")
        rangeoff.append("Td8c")

        rangeoff.append("Tc8s")
        rangeoff.append("Tc8h")
        rangeoff.append("Tc8d")
    elif "T7" in card1:
        rangeoff.append("Ts7h")
        rangeoff.append("Ts7d")
        rangeoff.append("Ts7c")

        rangeoff.append("Th7s")
        rangeoff.append("Th7d")
        rangeoff.append("Th7c")

        rangeoff.append("Td7s")
        rangeoff.append("Td7h")
        rangeoff.append("Td7c")

        rangeoff.append("Tc7s")
        rangeoff.append("Tc7h")
        rangeoff.append("Tc7d")
    elif "T6" in card1:
        rangeoff.append("Ts6h")
        rangeoff.append("Ts6d")
        rangeoff.append("Ts6c")

        rangeoff.append("Th6s")
        rangeoff.append("Th6d")
        rangeoff.append("Th6c")

        rangeoff.append("Td6s")
        rangeoff.append("Td6h")
        rangeoff.append("Td6c")

        rangeoff.append("Tc6s")
        rangeoff.append("Tc6h")
        rangeoff.append("Tc6d")
    elif "T5" in card1:
        rangeoff.append("Ts5h")
        rangeoff.append("Ts5d")
        rangeoff.append("Ts5c")

        rangeoff.append("Th5s")
        rangeoff.append("Th5d")
        rangeoff.append("Th5c")

        rangeoff.append("Td5s")
        rangeoff.append("Td5h")
        rangeoff.append("Td5c")

        rangeoff.append("Tc5s")
        rangeoff.append("Tc5h")
        rangeoff.append("Tc5d")
    elif "T4" in card1:
        rangeoff.append("Ts4h")
        rangeoff.append("Ts4d")
        rangeoff.append("Ts4c")

        rangeoff.append("Th4s")
        rangeoff.append("Th4d")
        rangeoff.append("Th4c")

        rangeoff.append("Td4s")
        rangeoff.append("Td4h")
        rangeoff.append("Td4c")

        rangeoff.append("Tc4s")
        rangeoff.append("Tc4h")
        rangeoff.append("Tc4d")
    elif "T3" in card1:
        rangeoff.append("Ts3h")
        rangeoff.append("Ts3d")
        rangeoff.append("Ts3c")

        rangeoff.append("Th3s")
        rangeoff.append("Th3d")
        rangeoff.append("Th3c")

        rangeoff.append("Td3s")
        rangeoff.append("Td3h")
        rangeoff.append("Td3c")

        rangeoff.append("Tc3s")
        rangeoff.append("Tc3h")
        rangeoff.append("Tc3d")
    elif "T2" in card1:
        rangeoff.append("Ts2h")
        rangeoff.append("Ts2d")
        rangeoff.append("Ts2c")

        rangeoff.append("Th2s")
        rangeoff.append("Th2d")
        rangeoff.append("Th2c")

        rangeoff.append("Td2s")
        rangeoff.append("Td2h")
        rangeoff.append("Td2c")

        rangeoff.append("Tc2s")
        rangeoff.append("Tc2h")
        rangeoff.append("Tc2d")
    elif "98" in card1:
        rangeoff.append("9s8h")
        rangeoff.append("9s8d")
        rangeoff.append("9s8c")

        rangeoff.append("9h8s")
        rangeoff.append("9h8d")
        rangeoff.append("9h8c")

        rangeoff.append("9d8s")
        rangeoff.append("9d8h")
        rangeoff.append("9d8c")

        rangeoff.append("9c8s")
        rangeoff.append("9c8h")
        rangeoff.append("9c8d")
    elif "97" in card1:
        rangeoff.append("9s7h")
        rangeoff.append("9s7d")
        rangeoff.append("9s7c")

        rangeoff.append("9h7s")
        rangeoff.append("9h7d")
        rangeoff.append("9h7c")

        rangeoff.append("9d7s")
        rangeoff.append("9d7h")
        rangeoff.append("9d7c")

        rangeoff.append("9c7s")
        rangeoff.append("9c7h")
        rangeoff.append("9c7d")
    elif "96" in card1:
        rangeoff.append("9s6h")
        rangeoff.append("9s6d")
        rangeoff.append("9s6c")

        rangeoff.append("9h6s")
        rangeoff.append("9h6d")
        rangeoff.append("9h6c")

        rangeoff.append("9d6s")
        rangeoff.append("9d6h")
        rangeoff.append("9d6c")

        rangeoff.append("9c6s")
        rangeoff.append("9c6h")
        rangeoff.append("9c6d")
    elif "95" in card1:
        rangeoff.append("9s5h")
        rangeoff.append("9s5d")
        rangeoff.append("9s5c")

        rangeoff.append("9h5s")
        rangeoff.append("9h5d")
        rangeoff.append("9h5c")

        rangeoff.append("9d5s")
        rangeoff.append("9d5h")
        rangeoff.append("9d5c")

        rangeoff.append("9c5s")
        rangeoff.append("9c5h")
        rangeoff.append("9c5d")
    elif "94" in card1:
        rangeoff.append("9s4h")
        rangeoff.append("9s4d")
        rangeoff.append("9s4c")

        rangeoff.append("9h4s")
        rangeoff.append("9h4d")
        rangeoff.append("9h4c")

        rangeoff.append("9d4s")
        rangeoff.append("9d4h")
        rangeoff.append("9d4c")

        rangeoff.append("9c4s")
        rangeoff.append("9c4h")
        rangeoff.append("9c4d")
    elif "93" in card1:
        rangeoff.append("9s3h")
        rangeoff.append("9s3d")
        rangeoff.append("9s3c")

        rangeoff.append("9h3s")
        rangeoff.append("9h3d")
        rangeoff.append("9h3c")

        rangeoff.append("9d3s")
        rangeoff.append("9d3h")
        rangeoff.append("9d3c")

        rangeoff.append("9c3s")
        rangeoff.append("9c3h")
        rangeoff.append("9c3d")
    elif "92" in card1:
        rangeoff.append("9s2h")
        rangeoff.append("9s2d")
        rangeoff.append("9s2c")

        rangeoff.append("9h2s")
        rangeoff.append("9h2d")
        rangeoff.append("9h2c")

        rangeoff.append("9d2s")
        rangeoff.append("9d2h")
        rangeoff.append("9d2c")

        rangeoff.append("9c2s")
        rangeoff.append("9c2h")
        rangeoff.append("9c2d")
    elif "87" in card1:
        rangeoff.append("8s7h")
        rangeoff.append("8s7d")
        rangeoff.append("8s7c")

        rangeoff.append("8h7s")
        rangeoff.append("8h7d")
        rangeoff.append("8h7c")

        rangeoff.append("8d7s")
        rangeoff.append("8d7h")
        rangeoff.append("8d7c")

        rangeoff.append("8c7s")
        rangeoff.append("8c7h")
        rangeoff.append("8c7d")
    elif "86" in card1:
        rangeoff.append("8s6h")
        rangeoff.append("8s6d")
        rangeoff.append("8s6c")

        rangeoff.append("8h6s")
        rangeoff.append("8h6d")
        rangeoff.append("8h6c")

        rangeoff.append("8d6s")
        rangeoff.append("8d6h")
        rangeoff.append("8d6c")

        rangeoff.append("8c6s")
        rangeoff.append("8c6h")
        rangeoff.append("8c6d")
    elif "85" in card1:
        rangeoff.append("8s5h")
        rangeoff.append("8s5d")
        rangeoff.append("8s5c")

        rangeoff.append("8h5s")
        rangeoff.append("8h5d")
        rangeoff.append("8h5c")

        rangeoff.append("8d5s")
        rangeoff.append("8d5h")
        rangeoff.append("8d5c")

        rangeoff.append("8c5s")
        rangeoff.append("8c5h")
        rangeoff.append("8c5d")
    elif "84" in card1:
        rangeoff.append("8s4h")
        rangeoff.append("8s4d")
        rangeoff.append("8s4c")

        rangeoff.append("8h4s")
        rangeoff.append("8h4d")
        rangeoff.append("8h4c")

        rangeoff.append("8d4s")
        rangeoff.append("8d4h")
        rangeoff.append("8d4c")

        rangeoff.append("8c4s")
        rangeoff.append("8c4h")
        rangeoff.append("8c4d")
    elif "83" in card1:
        rangeoff.append("8s3h")
        rangeoff.append("8s3d")
        rangeoff.append("8s3c")

        rangeoff.append("8h3s")
        rangeoff.append("8h3d")
        rangeoff.append("8h3c")

        rangeoff.append("8d3s")
        rangeoff.append("8d3h")
        rangeoff.append("8d3c")

        rangeoff.append("8c3s")
        rangeoff.append("8c3h")
        rangeoff.append("8c3d")
    elif "82" in card1:
        rangeoff.append("8s2h")
        rangeoff.append("8s2d")
        rangeoff.append("8s2c")

        rangeoff.append("8h2s")
        rangeoff.append("8h2d")
        rangeoff.append("8h2c")

        rangeoff.append("8d2s")
        rangeoff.append("8d2h")
        rangeoff.append("8d2c")

        rangeoff.append("8c2s")
        rangeoff.append("8c2h")
        rangeoff.append("8c2d")
    
    elif "76" in card1:
        rangeoff.append("7s6h")
        rangeoff.append("7s6d")
        rangeoff.append("7s6c")

        rangeoff.append("7h6s")
        rangeoff.append("7h6d")
        rangeoff.append("7h6c")

        rangeoff.append("7d6s")
        rangeoff.append("7d6h")
        rangeoff.append("7d6c")

        rangeoff.append("7c6s")
        rangeoff.append("7c6h")
        rangeoff.append("7c6d")
    elif "75" in card1:
        rangeoff.append("7s5h")
        rangeoff.append("7s5d")
        rangeoff.append("7s5c")

        rangeoff.append("7h5s")
        rangeoff.append("7h5d")
        rangeoff.append("7h5c")

        rangeoff.append("7d5s")
        rangeoff.append("7d5h")
        rangeoff.append("7d5c")

        rangeoff.append("7c5s")
        rangeoff.append("7c5h")
        rangeoff.append("7c5d")
    elif "74" in card1:
        rangeoff.append("7s4h")
        rangeoff.append("7s4d")
        rangeoff.append("7s4c")

        rangeoff.append("7h4s")
        rangeoff.append("7h4d")
        rangeoff.append("7h4c")

        rangeoff.append("7d4s")
        rangeoff.append("7d4h")
        rangeoff.append("7d4c")

        rangeoff.append("7c4s")
        rangeoff.append("7c4h")
        rangeoff.append("7c4d")
    elif "73" in card1:
        rangeoff.append("7s3h")
        rangeoff.append("7s3d")
        rangeoff.append("7s3c")

        rangeoff.append("7h3s")
        rangeoff.append("7h3d")
        rangeoff.append("7h3c")

        rangeoff.append("7d3s")
        rangeoff.append("7d3h")
        rangeoff.append("7d3c")

        rangeoff.append("7c3s")
        rangeoff.append("7c3h")
        rangeoff.append("7c3d")
    elif "72" in card1:
        rangeoff.append("7s2h")
        rangeoff.append("7s2d")
        rangeoff.append("7s2c")

        rangeoff.append("7h2s")
        rangeoff.append("7h2d")
        rangeoff.append("7h2c")

        rangeoff.append("7d2s")
        rangeoff.append("7d2h")
        rangeoff.append("7d2c")

        rangeoff.append("7c2s")
        rangeoff.append("7c2h")
        rangeoff.append("7c2d")
    
    elif "65" in card1:
        rangeoff.append("6s5h")
        rangeoff.append("6s5d")
        rangeoff.append("6s5c")

        rangeoff.append("6h5s")
        rangeoff.append("6h5d")
        rangeoff.append("6h5c")

        rangeoff.append("6d5s")
        rangeoff.append("6d5h")
        rangeoff.append("6d5c")

        rangeoff.append("6c5s")
        rangeoff.append("6c5h")
        rangeoff.append("6c5d")
    elif "64" in card1:
        rangeoff.append("6s4h")
        rangeoff.append("6s4d")
        rangeoff.append("6s4c")

        rangeoff.append("6h4s")
        rangeoff.append("6h4d")
        rangeoff.append("6h4c")

        rangeoff.append("6d4s")
        rangeoff.append("6d4h")
        rangeoff.append("6d4c")

        rangeoff.append("6c4s")
        rangeoff.append("6c4h")
        rangeoff.append("6c4d")
    elif "63" in card1:
        rangeoff.append("6s3h")
        rangeoff.append("6s3d")
        rangeoff.append("6s3c")

        rangeoff.append("6h3s")
        rangeoff.append("6h3d")
        rangeoff.append("6h3c")

        rangeoff.append("6d3s")
        rangeoff.append("6d3h")
        rangeoff.append("6d3c")

        rangeoff.append("6c3s")
        rangeoff.append("6c3h")
        rangeoff.append("6c3d")
    elif "62" in card1:
        rangeoff.append("6s2h")
        rangeoff.append("6s2d")
        rangeoff.append("6s2c")

        rangeoff.append("6h2s")
        rangeoff.append("6h2d")
        rangeoff.append("6h2c")

        rangeoff.append("6d2s")
        rangeoff.append("6d2h")
        rangeoff.append("6d2c")

        rangeoff.append("6c2s")
        rangeoff.append("6c2h")
        rangeoff.append("6c2d")
    
    elif "54" in card1:
        rangeoff.append("5s4h")
        rangeoff.append("5s4d")
        rangeoff.append("5s4c")

        rangeoff.append("5h4s")
        rangeoff.append("5h4d")
        rangeoff.append("5h4c")

        rangeoff.append("5d4s")
        rangeoff.append("5d4h")
        rangeoff.append("5d4c")

        rangeoff.append("5c4s")
        rangeoff.append("5c4h")
        rangeoff.append("5c4d")
    elif "53" in card1:
        rangeoff.append("5s3h")
        rangeoff.append("5s3d")
        rangeoff.append("5s3c")

        rangeoff.append("5h3s")
        rangeoff.append("5h3d")
        rangeoff.append("5h3c")

        rangeoff.append("5d3s")
        rangeoff.append("5d3h")
        rangeoff.append("5d3c")

        rangeoff.append("5c3s")
        rangeoff.append("5c3h")
        rangeoff.append("5c3d")
    elif "52" in card1:
        rangeoff.append("5s2h")
        rangeoff.append("5s2d")
        rangeoff.append("5s2c")

        rangeoff.append("5h2s")
        rangeoff.append("5h2d")
        rangeoff.append("5h2c")

        rangeoff.append("5d2s")
        rangeoff.append("5d2h")
        rangeoff.append("5d2c")

        rangeoff.append("5c2s")
        rangeoff.append("5c2h")
        rangeoff.append("5c2d")
    
    elif "43" in card1:
        rangeoff.append("4s3h")
        rangeoff.append("4s3d")
        rangeoff.append("4s3c")

        rangeoff.append("4h3s")
        rangeoff.append("4h3d")
        rangeoff.append("4h3c")

        rangeoff.append("4d3s")
        rangeoff.append("4d3h")
        rangeoff.append("4d3c")

        rangeoff.append("4c3s")
        rangeoff.append("4c3h")
        rangeoff.append("4c3d")
    elif "42" in card1:
        rangeoff.append("4s2h")
        rangeoff.append("4s2d")
        rangeoff.append("4s2c")

        rangeoff.append("4h2s")
        rangeoff.append("4h2d")
        rangeoff.append("4h2c")

        rangeoff.append("4d2s")
        rangeoff.append("4d2h")
        rangeoff.append("4d2c")

        rangeoff.append("4c2s")
        rangeoff.append("4c2h")
        rangeoff.append("4c2d")
    elif "32" in card1:
        rangeoff.append("3s2h")
        rangeoff.append("3s2d")
        rangeoff.append("3s2c")

        rangeoff.append("3h2s")
        rangeoff.append("3h2d")
        rangeoff.append("3h2c")

        rangeoff.append("3d2s")
        rangeoff.append("3d2h")
        rangeoff.append("3d2c")

        rangeoff.append("3c2s")
        rangeoff.append("3c2h")
        rangeoff.append("3c2d")
    return rangeoff

def expandPP(card1):
    rangepp = []
    if "A" in card1:
        rangepp.append("AsAh")
        rangepp.append("AsAd")
        rangepp.append("AsAc")

        rangepp.append("AhAd")
        rangepp.append("AhAc")

        rangepp.append("AdAc")
    elif "K" in card1:
        rangepp.append("KsKh")
        rangepp.append("KsKd")
        rangepp.append("KsKc")

        rangepp.append("KhKd")
        rangepp.append("KhKc")

        rangepp.append("KdKc")
    elif "Q" in card1:
        rangepp.append("QsQh")
        rangepp.append("QsQd")
        rangepp.append("QsQc")

        rangepp.append("QhQd")
        rangepp.append("QhQc")

        rangepp.append("QdQc")
    elif "J" in card1:
        rangepp.append("JsJh")
        rangepp.append("JsJd")
        rangepp.append("JsJc")

        rangepp.append("JhJd")
        rangepp.append("JhJc")

        rangepp.append("JdJc")
    elif "T" in card1:
        rangepp.append("TsTh")
        rangepp.append("TsTd")
        rangepp.append("TsTc")

        rangepp.append("ThTd")
        rangepp.append("ThTc")

        rangepp.append("TdTc")
    elif "9" in card1:
        rangepp.append("9s9h")
        rangepp.append("9s9d")
        rangepp.append("9s9c")

        rangepp.append("9h9d")
        rangepp.append("9h9c")

        rangepp.append("9d9c")
    elif "8" in card1:
        rangepp.append("8s8h")
        rangepp.append("8s8d")
        rangepp.append("8s8c")

        rangepp.append("8h8d")
        rangepp.append("8h8c")

        rangepp.append("8d8c")
    elif "7" in card1:
        rangepp.append("7s7h")
        rangepp.append("7s7d")
        rangepp.append("7s7c")

        rangepp.append("7h7d")
        rangepp.append("7h7c")

        rangepp.append("7d7c")
    elif "6" in card1:
        rangepp.append("6s6h")
        rangepp.append("6s6d")
        rangepp.append("6s6c")

        rangepp.append("6h6d")
        rangepp.append("6h6c")

        rangepp.append("6d6c")
    elif "5" in card1:
        rangepp.append("5s5h")
        rangepp.append("5s5d")
        rangepp.append("5s5c")

        rangepp.append("5h5d")
        rangepp.append("5h5c")

        rangepp.append("5d5c")
    elif "4" in card1:
        rangepp.append("4s4h")
        rangepp.append("4s4d")
        rangepp.append("4s4c")

        rangepp.append("4h4d")
        rangepp.append("4h4c")

        rangepp.append("4d4c")
    elif "3" in card1:
        rangepp.append("3s3h")
        rangepp.append("3s3d")
        rangepp.append("3s3c")

        rangepp.append("3h3d")
        rangepp.append("3h3c")

        rangepp.append("3d3c")
    elif "2" in card1:
        rangepp.append("2s2h")
        rangepp.append("2s2d")
        rangepp.append("2s2c")

        rangepp.append("2h2d")
        rangepp.append("2h2c")

        rangepp.append("2d2c")
    
    return rangepp



def expandSuit(card1):
    rangesuit = []
    if "AK" in card1:
        rangesuit.append("AsKs")
        rangesuit.append("AhKh")
        rangesuit.append("AdKd")
        rangesuit.append("AcKc")
    elif "AQ" in card1:
        rangesuit.append("AsQs")
        rangesuit.append("AhQh")
        rangesuit.append("AdQd")
        rangesuit.append("AcQc")
    elif "AJ" in card1:
        rangesuit.append("AsJs")
        rangesuit.append("AhJh")
        rangesuit.append("AdJd")
        rangesuit.append("AcJc")
    elif "AT" in card1:
        rangesuit.append("AsTs")
        rangesuit.append("AhTh")
        rangesuit.append("AdTd")
        rangesuit.append("AcTc")
    elif "A9" in card1:
        rangesuit.append("As9s")
        rangesuit.append("Ah9h")
        rangesuit.append("Ad9d")
        rangesuit.append("Ac9c")
    elif "A8" in card1:
        rangesuit.append("As8s")
        rangesuit.append("Ah8h")
        rangesuit.append("Ad8d")
        rangesuit.append("Ac8c")
    elif "A7" in card1:
        rangesuit.append("As7s")
        rangesuit.append("Ah7h")
        rangesuit.append("Ad7d")
        rangesuit.append("Ac7c")
    elif "A6" in card1:
        rangesuit.append("As6s")
        rangesuit.append("Ah6h")
        rangesuit.append("Ad6d")
        rangesuit.append("Ac6c")
    elif "A5" in card1:
        rangesuit.append("As5s")
        rangesuit.append("Ah5h")
        rangesuit.append("Ad5d")
        rangesuit.append("Ac5c")
    elif "A4" in card1:
        rangesuit.append("As4s")
        rangesuit.append("Ah4h")
        rangesuit.append("Ad4d")
        rangesuit.append("Ac4c")
    elif "A3" in card1:
        rangesuit.append("As3s")
        rangesuit.append("Ah3h")
        rangesuit.append("Ad3d")
        rangesuit.append("Ac3c")
    elif "A2" in card1:
        rangesuit.append("As2s")
        rangesuit.append("Ah2h")
        rangesuit.append("Ad2d")
        rangesuit.append("Ac2c")
    elif "KQ" in card1:
        rangesuit.append("KsQs")
        rangesuit.append("KhQh")
        rangesuit.append("KdQd")
        rangesuit.append("KcQc")
    elif "KJ" in card1:
        rangesuit.append("KsJs")
        rangesuit.append("KhJh")
        rangesuit.append("KdJd")
        rangesuit.append("KcJc")
    elif "KT" in card1:
        rangesuit.append("KsTs")
        rangesuit.append("KhTh")
        rangesuit.append("KdTd")
        rangesuit.append("KcTc")
    elif "K9" in card1:
        rangesuit.append("Ks9s")
        rangesuit.append("Kh9h")
        rangesuit.append("Kd9d")
        rangesuit.append("Kc9c")
    elif "K8" in card1:
        rangesuit.append("Ks8s")
        rangesuit.append("Kh8h")
        rangesuit.append("Kd8d")
        rangesuit.append("Kc8c")
    elif "K7" in card1:
        rangesuit.append("Ks7s")
        rangesuit.append("Kh7h")
        rangesuit.append("Kd7d")
        rangesuit.append("Kc7c")
    elif "K6" in card1:
        rangesuit.append("Ks6s")
        rangesuit.append("Kh6h")
        rangesuit.append("Kd6d")
        rangesuit.append("Kc6c")
    elif "K5" in card1:
        rangesuit.append("Ks5s")
        rangesuit.append("Kh5h")
        rangesuit.append("Kd5d")
        rangesuit.append("Kc5c")
    elif "K4" in card1:
        rangesuit.append("Ks4s")
        rangesuit.append("Kh4h")
        rangesuit.append("Kd4d")
        rangesuit.append("Kc4c")
    elif "K3" in card1:
        rangesuit.append("Ks3s")
        rangesuit.append("Kh3h")
        rangesuit.append("Kd3d")
        rangesuit.append("Kc3c")
    elif "K2" in card1:
        rangesuit.append("Ks2s")
        rangesuit.append("Kh2h")
        rangesuit.append("Kd2d")
        rangesuit.append("Kc2c")
    elif "QJ" in card1:
        rangesuit.append("QsJs")
        rangesuit.append("QhJh")
        rangesuit.append("QdJd")
        rangesuit.append("QcJc")
    elif "QT" in card1:
        rangesuit.append("QsTs")
        rangesuit.append("QhTh")
        rangesuit.append("QdTd")
        rangesuit.append("QcTc")
    elif "Q9" in card1:
        rangesuit.append("Qs9s")
        rangesuit.append("Qh9h")
        rangesuit.append("Qd9d")
        rangesuit.append("Qc9c")
    elif "Q8" in card1:
        rangesuit.append("Qs8s")
        rangesuit.append("Qh8h")
        rangesuit.append("Qd8d")
        rangesuit.append("Qc8c")
    elif "Q7" in card1:
        rangesuit.append("Qs7s")
        rangesuit.append("Qh7h")
        rangesuit.append("Qd7d")
        rangesuit.append("Qc7c")
    elif "Q6" in card1:
        rangesuit.append("Qs6s")
        rangesuit.append("Qh6h")
        rangesuit.append("Qd6d")
        rangesuit.append("Qc6c")
    elif "Q5" in card1:
        rangesuit.append("Qs5s")
        rangesuit.append("Qh5h")
        rangesuit.append("Qd5d")
        rangesuit.append("Qc5c")
    elif "Q4" in card1:
        rangesuit.append("Qs4s")
        rangesuit.append("Qh4h")
        rangesuit.append("Qd4d")
        rangesuit.append("Qc4c")
    elif "Q3" in card1:
        rangesuit.append("Qs3s")
        rangesuit.append("Qh3h")
        rangesuit.append("Qd3d")
        rangesuit.append("Qc3c")
    elif "Q2" in card1:
        rangesuit.append("Qs2s")
        rangesuit.append("Qh2h")
        rangesuit.append("Qd2d")
        rangesuit.append("Qc2c")
    elif "JT" in card1:
        rangesuit.append("JsTs")
        rangesuit.append("JhTh")
        rangesuit.append("JdTd")
        rangesuit.append("JcTc")
    elif "J9" in card1:
        rangesuit.append("Js9s")
        rangesuit.append("Jh9h")
        rangesuit.append("Jd9d")
        rangesuit.append("Jc9c")
    elif "J8" in card1:
        rangesuit.append("Js8s")
        rangesuit.append("Jh8h")
        rangesuit.append("Jd8d")
        rangesuit.append("Jc8c")
    elif "J7" in card1:
        rangesuit.append("Js7s")
        rangesuit.append("Jh7h")
        rangesuit.append("Jd7d")
        rangesuit.append("Jc7c")
    elif "J6" in card1:
        rangesuit.append("Js6s")
        rangesuit.append("Jh6h")
        rangesuit.append("Jd6d")
        rangesuit.append("Jc6c")
    elif "J5" in card1:
        rangesuit.append("Js5s")
        rangesuit.append("Jh5h")
        rangesuit.append("Jd5d")
        rangesuit.append("Jc5c")
    elif "J4" in card1:
        rangesuit.append("Js4s")
        rangesuit.append("Jh4h")
        rangesuit.append("Jd4d")
        rangesuit.append("Jc4c")
    elif "J3" in card1:
        rangesuit.append("Js3s")
        rangesuit.append("Jh3h")
        rangesuit.append("Jd3d")
        rangesuit.append("Jc3c")
    elif "J2" in card1:
        rangesuit.append("Js2s")
        rangesuit.append("Jh2h")
        rangesuit.append("Jd2d")
        rangesuit.append("Jc2c")
    elif "T9" in card1:
        rangesuit.append("Ts9s")
        rangesuit.append("Th9h")
        rangesuit.append("Td9d")
        rangesuit.append("Tc9c")
    elif "T8" in card1:
        rangesuit.append("Ts8s")
        rangesuit.append("Th8h")
        rangesuit.append("Td8d")
        rangesuit.append("Tc8c")
    elif "T7" in card1:
        rangesuit.append("Ts7s")
        rangesuit.append("Th7h")
        rangesuit.append("Td7d")
        rangesuit.append("Tc7c")
    elif "T6" in card1:
        rangesuit.append("Ts6s")
        rangesuit.append("Th6h")
        rangesuit.append("Td6d")
        rangesuit.append("Tc6c")
    elif "T5" in card1:
        rangesuit.append("Ts5s")
        rangesuit.append("Th5h")
        rangesuit.append("Td5d")
        rangesuit.append("Tc5c")
    elif "T4" in card1:
        rangesuit.append("Ts4s")
        rangesuit.append("Th4h")
        rangesuit.append("Td4d")
        rangesuit.append("Tc4c")
    elif "T3" in card1:
        rangesuit.append("Ts3s")
        rangesuit.append("Th3h")
        rangesuit.append("Td3d")
        rangesuit.append("Tc3c")
    elif "T2" in card1:
        rangesuit.append("Ts2s")
        rangesuit.append("Th2h")
        rangesuit.append("Td2d")
        rangesuit.append("Tc2c")
    elif "98" in card1:
        rangesuit.append("9s8s")
        rangesuit.append("9h8h")
        rangesuit.append("9d8d")
        rangesuit.append("9c8c")
    elif "97" in card1:
        rangesuit.append("9s7s")
        rangesuit.append("9h7h")
        rangesuit.append("9d7d")
        rangesuit.append("9c7c")
    elif "96" in card1:
        rangesuit.append("9s6s")
        rangesuit.append("9h6h")
        rangesuit.append("9d6d")
        rangesuit.append("9c6c")
    elif "95" in card1:
        rangesuit.append("9s5s")
        rangesuit.append("9h5h")
        rangesuit.append("9d5d")
        rangesuit.append("9c5c")
    elif "94" in card1:
        rangesuit.append("9s4s")
        rangesuit.append("9h4h")
        rangesuit.append("9d4d")
        rangesuit.append("9c4c")
    elif "93" in card1:
        rangesuit.append("9s3s")
        rangesuit.append("9h3h")
        rangesuit.append("9d3d")
        rangesuit.append("9c3c")
    elif "92" in card1:
        rangesuit.append("9s2s")
        rangesuit.append("9h2h")
        rangesuit.append("9d2d")
        rangesuit.append("9c2c")
    elif "87" in card1:
        rangesuit.append("8s7s")
        rangesuit.append("8h7h")
        rangesuit.append("8d7d")
        rangesuit.append("8c7c")
    elif "86" in card1:
        rangesuit.append("8s6s")
        rangesuit.append("8h6h")
        rangesuit.append("8d6d")
        rangesuit.append("8c6c")
    elif "85" in card1:
        rangesuit.append("8s5s")
        rangesuit.append("8h5h")
        rangesuit.append("8d5d")
        rangesuit.append("8c5c")
    elif "84" in card1:
        rangesuit.append("8s4s")
        rangesuit.append("8h4h")
        rangesuit.append("8d4d")
        rangesuit.append("8c4c")
    elif "83" in card1:
        rangesuit.append("8s3s")
        rangesuit.append("8h3h")
        rangesuit.append("8d3d")
        rangesuit.append("8c3c")
    elif "82" in card1:
        rangesuit.append("8s2s")
        rangesuit.append("8h2h")
        rangesuit.append("8d2d")
        rangesuit.append("8c2c")
    elif "76" in card1:
        rangesuit.append("7s6s")
        rangesuit.append("7h6h")
        rangesuit.append("7d6d")
        rangesuit.append("7c6c")
    elif "75" in card1:
        rangesuit.append("7s5s")
        rangesuit.append("7h5h")
        rangesuit.append("7d5d")
        rangesuit.append("7c5c")
    elif "74" in card1:
        rangesuit.append("7s4s")
        rangesuit.append("7h4h")
        rangesuit.append("7d4d")
        rangesuit.append("7c4c")
    elif "73" in card1:
        rangesuit.append("7s3s")
        rangesuit.append("7h3h")
        rangesuit.append("7d3d")
        rangesuit.append("7c3c")
    elif "72" in card1:
        rangesuit.append("7s2s")
        rangesuit.append("7h2h")
        rangesuit.append("7d2d")
        rangesuit.append("7c2c")
    elif "65" in card1:
        rangesuit.append("6s5s")
        rangesuit.append("6h5h")
        rangesuit.append("6d5d")
        rangesuit.append("6c5c")
    elif "64" in card1:
        rangesuit.append("6s4s")
        rangesuit.append("6h4h")
        rangesuit.append("6d4d")
        rangesuit.append("6c4c")
    elif "63" in card1:
        rangesuit.append("6s3s")
        rangesuit.append("6h3h")
        rangesuit.append("6d3d")
        rangesuit.append("6c3c")
    elif "62" in card1:
        rangesuit.append("6s2s")
        rangesuit.append("6h2h")
        rangesuit.append("6d2d")
        rangesuit.append("6c2c")
    elif "54" in card1:
        rangesuit.append("5s4s")
        rangesuit.append("5h4h")
        rangesuit.append("5d4d")
        rangesuit.append("5c4c")
    elif "53" in card1:
        rangesuit.append("5s3s")
        rangesuit.append("5h3h")
        rangesuit.append("5d3d")
        rangesuit.append("5c3c")
    elif "52" in card1:
        rangesuit.append("5s2s")
        rangesuit.append("5h2h")
        rangesuit.append("5d2d")
        rangesuit.append("5c2c")
    elif "43" in card1:
        rangesuit.append("4s3s")
        rangesuit.append("4h3h")
        rangesuit.append("4d3d")
        rangesuit.append("4c3c")
    elif "42" in card1:
        rangesuit.append("4s2s")
        rangesuit.append("4h2h")
        rangesuit.append("4d2d")
        rangesuit.append("4c2c")
    elif "32" in card1:
        rangesuit.append("3s2s")
        rangesuit.append("3h2h")
        rangesuit.append("3d2d")
        rangesuit.append("3c2c")

    

    return rangesuit
    