# salva_xml
Transforma dados salvo em tabela do Sankhya em arquivos xml separados

- Salvar os dados da tabela TGFNFE, apenas a coluna XML, em um arquivo .csv;
- Salvar o arquivo gerado na pasta do script;
- Rodar o script indicando o nome do arquivo sem a extensão.

O script pega a chave da nfe para criar o arquivo xml e usa como nome
O nome da pasta criada onde os xmls sao salvos é o mesmo nome do arquivo original caputarado do banco sem a extensão.

O script inicialmente leva 20 segundos para criar 50 mil arquivos xml.

```sql
-- NOTAS DE SAÍDA
SELECT [XML] 
FROM TGFNFE WHERE NUNOTA IN (
SELECT DISTINCT NUNOTA FROM TGFCAB WHERE YEAR(DTNEG)=2023)

```
```sql
-- NOTAS DE ENTRADA
SELECT [XML] 
FROM TGFIXN WHERE NUNOTA IN (
SELECT DISTINCT NUNOTA FROM TGFCAB WHERE YEAR(DTNEG)=2023)
AND [XML] IS NOT NULL

```
