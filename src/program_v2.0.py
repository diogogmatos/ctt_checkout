# LIBRARIES

from simple_term_menu import TerminalMenu

from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import requests

# WEB SCRAPING

print("""-- INICIALIZAÇÃO --
\nAtualizando a base de dados...""")

# embalagens

page_emb = requests.get("https://www.ctt.pt/particulares/enviar/caixas-e-saquetas")
soup_emb = bs(page_emb.content, features="html5lib")
precos_emb = [i.text for i in soup_emb.find_all(style="text-align: center;")]

s0 = precos_emb[1]
s1 = precos_emb[2]
s2 = precos_emb[3]
s3 = precos_emb[4]

c0 = precos_emb[9]
c1 = precos_emb[10]
c2 = precos_emb[11]
c3 = precos_emb[12]
c4 = precos_emb[13]

# correio editorial

page_editorial = requests.get("https://www.ctt.pt/empresas/solucoes-de-gestao-e-setoriais/solucoes-setoriais/editores-e-livreiros/correio-editorial-nacional")
soup_editorial = bs(page_editorial.content, features="html5lib")
precos_editorial = [i.text for i in soup_editorial.find_all(style="text-align: center;")]

e0 = precos_editorial[17]
e1 = precos_editorial[18]
e2 = precos_editorial[19]
e3 = precos_editorial[20]

# serviços adicionais

precos_sa0 = [i.text for i in soup_editorial.find_all("span")]

sa0 = precos_sa0[36]

precos_sa1 = [i.text for i in soup_editorial.find_all("ul")]

sa1 = precos_sa1[30][25:]

sa2 = precos_editorial[42]

precos_sa3 = [i.text for i in soup_editorial.find_all("p")]

sa3 = precos_sa3[62]

# saco multipostal

page_saco = requests.get("https://www.ctt.pt/empresas/solucoes-de-gestao-e-setoriais/solucoes-setoriais/editores-e-livreiros/saco-multipostal-nacional")
soup_saco = bs(page_saco.content, features="html5lib")
precos_saco = [i.text for i in soup_saco.find_all(style="text-align: center;")]

sm0 = precos_saco[3] # Portugal Continental
sm1 = precos_saco[4] # Açores e Madeira

# correio normal

page_normal = requests.get("https://www.ctt.pt/particulares/enviar/para-portugal/correio-normal")
soup_normal = bs(page_normal.content, features="html5lib")
precos_normal = [i.text for i in soup_normal.find_all(style="text-align: center;")]

n0 = precos_normal[10]
n1 = precos_normal[13]

n2 = precos_normal[11]
n3 = precos_normal[14]

n4 = precos_normal[12]
n5 = precos_normal[21]
n6 = precos_normal[24]

# correio azul

page_azul = requests.get("https://www.ctt.pt/particulares/enviar/para-portugal/correio-azul")
soup_azul = bs(page_azul.content, features="html5lib")
precos_azul = [i.text for i in soup_azul.find_all(style="text-align: center;")]

a0 = precos_azul[10]
a1 = precos_azul[13]

a2 = precos_azul[11]
a3 = precos_azul[14]

a4 = precos_azul[12]
a5 = precos_azul[21]
a6 = precos_azul[24]

# função de conversão

def to_val(str, type):

    if type == "editorial": # Correio Editorial

        obj = float(str[0] + "." + str[2] + str[3] + str[4])
        kg = float(str[21] + "." + str[23] + str[24] + str[25])

        return obj, kg

    elif type == "emb": # Embalagens

        n = float(str[0] + "." + str[2] + str[3])
        r = n + 0.23 * n # Soma do valor do IVA

        return r
    
    else: # Outros

        r = float(str[0] + "." + str[2] + str[3])

        return r

# VALUES

# saquetas

val_saqueta_s = to_val(s0, "emb")
val_saqueta_m = to_val(s1, "emb")
val_saqueta_l = to_val(s2, "emb")
val_saqueta_xl = to_val(s3, "emb")

# caixas

val_caixa_xs = to_val(c0, "emb")
val_caixa_m = to_val(c1, "emb")
val_caixa_l = to_val(c2, "emb")
val_caixa_xl = to_val(c3, "emb")
val_caixa_g = to_val(c4, "emb")

# serviços adicionais

val_ser = to_val(sa0, 0) # Serviço Especial Registo
val_ce = to_val(sa1, 0)  # Comprovativo Entrega
val_ec = to_val(sa2, 0)  # Envio à Cobrança
val_sms = to_val(sa3, 0) # Avisos por email e SMS

# correio editorial

val_e_100_obj, val_e_100_kg = to_val(e0, "editorial")  # Editorial | <100g
val_e_250_obj, val_e_250_kg = to_val(e1, "editorial")  # Editorial | >100g and <=250g
val_e_500_obj, val_e_500_kg = to_val(e2, "editorial")  # Editorial | >250g and <=500g
val_e_2000_obj,val_e_2000_kg = to_val(e3, "editorial") # Editorial | >500g and <=2000g
val_e_5000_pc = to_val(sm0, 0)                          # Editorial | Portugal Continental
val_e_5000_am = to_val(sm1, 0)                          # Editorial | Açores e Madeira

# correio normal

val_n_norm_20 = to_val(n0, 0)    # Normal Normalizado | <20g
val_n_norm_else = to_val(n1, 0)  # Normal Normalizado | >20g and <=50g
val_n_nnorm_20 = to_val(n2, 0)   # Normal Não Normalizado | <20g
val_n_nnorm_else = to_val(n3, 0) # Normal Não Normalizado | >20g and <=50g
val_n_pp_100 = to_val(n4, 0)     # Normal Pacote Postal | <100g
val_n_pp_500 = to_val(n5, 0)     # Normal Pacote Postal | >100g and <=500g
val_n_pp_2000 = to_val(n6, 0)    # Normal Pacote Postal | >500g and <=2000g

# correio azul

val_a_norm_20 = to_val(a0, 0)    # Azul Normalizado | <20g
val_a_norm_else = to_val(a1, 0)  # Azul Normalizado | >20g and <=50g
val_a_nnorm_20 = to_val(a2, 0)   # Azul Não Normalizado | <20g
val_a_nnrom_else = to_val(a3, 0) # Azul Não Normalizado | >20g and <=50g
val_a_pp_100 = to_val(a4, 0)     # Azul Pacote Postal | <100g
val_a_pp_500 = to_val(a5, 0)     # Azul Pacote Postal | >100g and <=500g
val_a_pp_2000 = to_val(a6, 0)    # Azul Pacote Postal | >500g and <=2000g

#end

print("> Sucesso!")

# OPÇÕES DE ENVIO

def embalagem(peso): # Seleção de Embalagem
    
    emb_options = ["SAQUETA ALMOFADADA", "CAIXA", "IGNORAR"]
    emb_menu = TerminalMenu(emb_options, title="Seleção de Embalagem")
    sel = emb_menu.show()

    if sel == 0: # Saqueta
        
        saqueta_options = ["S", "M", "L", "XL"]
        saqueta_menu = TerminalMenu(saqueta_options, title="Tamanho da Saqueta")
        saqueta = saqueta_menu.show()
        
        if saqueta == 0: # S
            peso += 16
            pemb = val_saqueta_s
        elif saqueta == 1: # M
            peso += 22
            pemb = val_saqueta_m
        elif saqueta == 2: # L
            peso += 35
            pemb = val_saqueta_l
        else: # XL
            peso += 60
            pemb = val_saqueta_xl
        
    elif sel == 1: # Caixa

        caixa_options = ["XS", "M", "L", "XL", "GARRAFA"]
        caixa_menu = TerminalMenu(caixa_options, title="Tamanho da Caixa")
        caixa = caixa_menu.show()

        if caixa == 0: # XS
            peso += 82
            pemb = val_caixa_xs
        elif caixa == 1: # M
            peso += 143
            pemb = val_caixa_m
        elif caixa == 2: # L
            peso += 226
            pemb = val_caixa_l
        elif caixa == 3: # XL
            peso += 392
            pemb = val_caixa_xl
        else: # PARA GARRAFA
            peso += 130
            pemb = val_caixa_g
    
    else:
        pemb = 0

    return peso, pemb

def sa(): # Serviços Adicionais
    
    options = [
    "Serviço Especial de Registo",
    "Comprovativo de Entrega (Aviso de Receção)",
    "Envio à Cobrança (até 2500 EUR)",
    "Alertas por email e SMS"]

    menu = TerminalMenu(
    options,
    multi_select=True,
    show_multi_select_hint=True,
    multi_select_select_on_accept=False,
    multi_select_empty_ok=True,
    title="Serviços adicionais")

    menu._show_multi_select_hint_text = "(Pressione ESPAÇO ou TAB para selecionar um ou múltiplos serviços. Pressione ENTER para submeter.)"
    menu.show()
    selected = menu.chosen_menu_entries

    pser = 0
    pce = 0
    pec = 0
    sms = 0

    if selected != None:
        if "Serviço Especial de Registo" in selected: # Serviço Especial de Registo
            pser = val_ser
        if "Comprovativo de Entrega (Aviso de Receção)" in selected: # Comprovativo de Entrega
            pce = val_ce + pser 
        if "Envio à Cobrança (até 2500 EUR)" in selected: # Envio à Cobrança
            pec = val_ec + pser
        if "Alertas por email e SMS" in selected:
            sms = val_sms
                            
    return pser, pce, pec, sms

# CÁLCULO/IMPRESSÃO DO PREÇO FINAL

def preco(penvio, pemb, pser, pce, pec, sms, peso, tipo):
    
    preco = penvio + pemb + pser + pce + pec + sms

    print("----------------- RESUMO -----------------\n")
    print(f"Tipo de envio: {tipo}")
    print(f"Peso total (artigo + embalagem): {peso}g\n")
    print(f"Envio:                          {penvio:.2f} EUR")
    if pemb != 0: print(f"Embalagem:                      {pemb:.2f} EUR")
    if pser != 0: print(f"Serviço Especial Registo:       {pser:.2f} EUR")
    if pce != 0: print(f"Comprovativo de Entrega:        {pce:.2f} EUR")
    if pec != 0: print(f"Envio à Cobrança:               {pec:.2f} EUR")
    if sms != 0: print(f"Alertas por email e SMS:        {sms:.2f} EUR")
    print(f"TOTAL:                          {preco:.2f} EUR")
    print("\n*NOTA: Valor do IVA incluído")
    print("\n------------------------------------------\n")

    return preco

# TIPOS DE CORREIO

def editorial(): # Correio Editorial
    
    state = 0
    while state != 1:
        
        print("Digite o número de livros a serem enviados: ", end = '')
        num = int(input())

        print("\nDigite o peso do livro ou conjunto de livros (em gramas): ", end = '')
        p = int(input())
        print()

        if p > 5000:
            print("""-- ERRO --
            \nO artigo ultrapassa o peso máximo que pode ser calculado (2Kg)
            \n----------\n""")
        else:
            
            p, pemb = embalagem(p)
            pser, pce, pec, sms = sa()

            if p <= 100:
                penvio = val_e_100_obj * num + (val_e_100_kg * p) / 1000
                preco(penvio, pemb, pser, pce, pec, sms, p, "EDITORIAL")
            elif p > 100 and p <= 250:
                penvio = val_e_250_obj * num + (val_e_250_kg * p) / 1000
                preco(penvio, pemb, pser, pce, pec, sms, p, "EDITORIAL")
            elif p > 250 and p <= 500:
                penvio = val_e_500_obj * num + (val_e_500_kg * p) / 1000
                preco(penvio, pemb, pser, pce, pec, sms, p, "EDITORIAL")
            elif p > 500 and p <= 2000:
                penvio = val_e_2000_obj * num + (val_e_2000_kg * p) / 1000
                preco(penvio, pemb, pser, pce, pec, sms, p, "EDITORIAL")
            elif p > 2000 and p <= 5000:
                
                local_options = ["Portugal continental", "Açores e Madeira"]
                local_menu = TerminalMenu(local_options, title="Qual o local de origem?")
                local = local_menu.show()

                if local == 0:
                    num = val_e_5000_pc
                else:
                    num = val_e_5000_am

                penvio = val_e_2000_obj * num + (val_e_2000_kg * p) / 1000 + num * int(str(p)[0])

                preco(penvio, pemb, pser, pce, pec, sms, p, "EDITORIAL")

            else:
                print(f"""-- ERRO --
                \nO conjunto 'artigo + embalagem' ultrapassa o peso máximo que pode ser calculado (2Kg)
                \nPeso do conjunto: {p} gramas
                \n----------""")

            print("Prazo de entrega: Cerca de 3 dias úteis\n")

        repeat_options = ["SIM", "NÃO"]
        repeat_menu = TerminalMenu(repeat_options, title="Calcular novamente?")
        state = repeat_menu.show()

    pass

def normal(): # Correio Normal
    
    state = 0
    while state != 1:
        
        options = ["Documento Normalizado", "Documento Não Normalizado", "Bens/Documentos em Pacote Postal"]
        menu = TerminalMenu(options, show_search_hint=True, title="Tipo de artigo")
        menu._show_search_hint_text = "Saiba mais sobre normalização em: https://www.ctt.pt/empresas/encomendas-e-correio/enviar/regras-e-cuidados-para-envios/normalizacao"
        sel = menu.show()

        print("Digite o peso do artigo (em gramas): ", end = '')
        peso = input()
        p = int(peso)
        print()

        if sel == 0: # Documento Normalizado

            if p > 50:
                print("""-- ERRO --
                \nO artigo ultrapassa o peso máximo que pode ser calculado (2Kg)
                \n----------\n""")
            else:

                if p <= 20:
                    penvio = val_n_norm_20
                else:
                    penvio = val_n_norm_else

                preco(penvio, 0, 0, 0, 0, 0, p, "NORMAL")

        elif sel == 1: # Documento Não Normalizado

            if p > 100:
                print("""-- ERRO --
                \nO artigo ultrapassa o peso máximo que pode ser calculado (2Kg)
                \n----------\n""")
            else:

                if p <= 20:
                    penvio = val_n_nnorm_20
                else:
                    penvio = val_n_nnorm_else

                preco(penvio, 0, 0, 0, 0, 0, p, "NORMAL")
            
        else: # Bens/Documentos em Pacote Postal

            if p > 2000:
                print("""-- ERRO --
                \nO artigo ultrapassa o peso máximo que pode ser calculado (2Kg)
                \n----------\n""")
            else:

                p, pemb = embalagem(p)

                if p <= 100:
                    penvio = val_n_pp_100
                    preco(penvio, pemb, 0, 0, 0, 0, p, "NORMAL")
                elif p > 100 and p <= 500:
                    penvio = val_n_pp_500
                    preco(penvio, pemb, 0, 0, 0, 0, p, "NORMAL")
                elif p > 500 and p <= 2000:
                    penvio = val_n_pp_2000
                    preco(penvio, pemb, 0, 0, 0, 0, p, "NORMAL")
                else:
                    print(f"""-- ERRO --
                    \nO conjunto 'artigo + embalagem' ultrapassa o peso máximo que pode ser calculado (2Kg)
                    \nPeso do conjunto: {p} gramas
                    \n----------""")

        print("Prazo de entrega: Cerca de 3 dias úteis\n")
            
        repeat_options = ["SIM", "NÃO"]
        repeat_menu = TerminalMenu(repeat_options, title="Calcular novamente?")
        state = repeat_menu.show()

    pass

def azul(): # Correio Azul
    
    state = 0
    while state != 1:
        
        options = ["Documento Normalizado", "Documento Não Normalizado", "Bens/Documentos em Pacote Postal"]
        menu = TerminalMenu(options, show_search_hint=True, title="Tipo de artigo")
        menu._show_search_hint_text = "Saiba mais sobre normalização em: https://www.ctt.pt/empresas/encomendas-e-correio/enviar/regras-e-cuidados-para-envios/normalizacao"
        sel = menu.show()

        print("Digite o peso do artigo (em gramas): ", end = '')
        peso = input()
        p = int(peso)
        print()

        if sel == 0: # Documento Normalizado

            if p > 50:
                print("""-- ERRO --
                \nO artigo ultrapassa o peso máximo que pode ser calculado (2Kg)
                \n----------\n""")
            else:

                if p <= 20:
                    penvio = val_a_norm_20
                else:
                    penvio = val_a_norm_else

                preco(penvio, 0, 0, 0, 0, 0, p, "AZUL")

        elif sel == 1: # Documento Não Normalizado

            if p > 100:
                print("""-- ERRO --
                \nO artigo ultrapassa o peso máximo que pode ser calculado (2Kg)
                \n----------\n""")
            else:

                if p <= 20:
                    penvio = val_a_nnorm_20
                else:
                    penvio = val_a_nnrom_else

                preco(penvio, 0, 0, 0, 0, 0, p, "AZUL")
            
        else: # Bens/Documentos em Pacote Postal

            if p > 2000:
                print("""-- ERRO --
                \nO artigo ultrapassa o peso máximo que pode ser calculado (2Kg)
                \n----------\n""")
            else:

                p, pemb = embalagem(p)

                if p <= 100:
                    penvio = val_a_pp_100
                    preco(penvio, pemb, 0, 0, 0, 0, p, "AZUL")
                elif p > 100 and p <= 500:
                    penvio = val_a_pp_500
                    preco(penvio, pemb, 0, 0, 0, 0, p, "AZUL")
                elif p > 500 and p <= 2000:
                    penvio = val_a_pp_2000
                    preco(penvio, pemb, 0, 0, 0, 0, p, "AZUL")
                else:
                    print(f"""-- ERRO --
                    \nO conjunto 'artigo + embalagem' ultrapassa o peso máximo que pode ser calculado (2Kg)
                    \nPeso do conjunto: {p} gramas
                    \n----------""")

        print("Prazo de entrega: Cerca de 1 dia útil\n")
            
        repeat_options = ["SIM", "NÃO"]
        repeat_menu = TerminalMenu(repeat_options, title="Calcular novamente?")
        state = repeat_menu.show()

    pass

# MAIN

print("""\n-- CTT CHECKOUT --
\nEsta aplicação permite simular o preço de envio de um artigo via CTT por diversas modalidades
> Modalidades suportadas: CORREIO EDITORIAL, CORRREIO NORMAL, CORREIO AZUL (+ em breve)
\n> NOTA: Estão incluídas as opções de embalagem que os CTT oferecem (Saquetas e Caixas), o respetivo peso e preço são incluídos no cálculo final
\n> AVISO: Os valores apresentados servem meramente como uma aproximação baseada nos preçários disponibilizados em ctt.pt
\n------------------\n""")

estado = 0
while estado != 1:
    
    correio_options = ["CORREIO EDITORIAL (LIVROS)", "CORREIO NORMAL (+ECONÓMICO)", "CORREIO AZUL (+RÁPIDO)"]
    correio_menu = TerminalMenu(correio_options, title="Como pretende enviar o seu artigo?")
    opcao = correio_menu.show()

    if opcao == 0:
        editorial()
    elif opcao == 1:
        normal()
    else:
        azul()
    
    end_options = ["NOVA SIMULAÇÃO", "SAIR DO PROGRAMA"]
    end_menu = TerminalMenu(end_options, title="MENU")
    estado = end_menu.show()
