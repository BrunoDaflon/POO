import java.util.Scanner;

public class Banco {
    // Atributos
    public String banco;
    public String agencia;
    public int conta;
    public String cliente;
    public String cpf;
    public double saldo;
    public double caixinha;
    public Integer tempo_investimento;
    public double taxajuros;
    public String senha;

    // Método Construtor
    public Banco(String banco, String agencia, int conta, String cliente, String cpf) {
        this.banco = banco;
        this.agencia = agencia;
        this.conta = conta;
        this.cliente = cliente;
        this.cpf = cpf;
        this.saldo = 0;
        this.caixinha = 0;
        this.tempo_investimento = null;
        this.taxajuros = 0.005;
        this.senha = null;
    }

    // Métodos da classe
    // Método de criar senha
    public void definirsenha(String novasenha) {
        if (this.senha == null) {
            this.senha = novasenha;
            System.out.println("Sua senha foi definida");
        } else {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Você já possuí uma senha definida, deseja mudar a sua senha? (sim/não): ");
            String decisao = scanner.nextLine().toLowerCase();
            if (decisao.equals("sim")) {
                this.senha = novasenha;
                System.out.println("Senah alterada com sucesso!");
            } else {
                System.out.println("Opção canelada!");
            }
        }
    }

    // Método de deposito
    public void deposito(double valor) {
        if (valor > 0) {
            this.saldo += valor;
            System.out.printf("Saldo atualizado com sucesso no valor R$%.2f.\n", valor);
        } else {
            System.out.println("Valor invalido par ao deposito");
        }
    }

    // Método de saque
    public void saque(String senha, double valor) {
        if(this.senha.equals(senha) && this.saldo >= valor && valor > 0) {
            this.saldo -= valor;
            System.out.printf("Saque realizado no valor de: R$%.2f.\n", valor);
        } else {
            System.out.println("Valor ou senha incorreto, tente novamente!");
        }
    }

    // Método de Pix
    public void pix(Banco destinatario, double valor) {
        if (valor > 0 && this.saldo >= valor) {
            this.saldo -= valor;
            destinatario.saldo += valor;
            System.out.printf("Pix realizado no valor R$%.2f\n DE: %s \n Para: %s", valor, this.cliente, destinatario.cliente);
        } else {
            System.out.println("Valor menor que zero ou inserido de forma errad, ou saldo menor que o valor definido!");
        }
    }

    // Método de caixinha
    public void caixinha_invest(double valor, int tempoMeses) {
        if(valor > 0 && this.saldo >= valor) {
            this.saldo -= valor;
            this.caixinha += valor;
            this.tempo_investimento = tempoMeses;
            System.out.printf("Valor de R%.2f transferido para a caixinha por %d meses. \n", valor, tempoMeses);
        } else {
            System.out.println("Valor menor ou igual a 0 ou saldo menor que o valor definido");
        }
    }

    // Método calcular rendimento
    public void calular_rendimento() {
        if(this.tempo_investimento != null && this.caixinha > 0) {
            // juros compostos:  M = C *(1+i)^t
            double montante = this.caixinha  * Math.pow(1 + this.taxajuros, this.tempo_investimento);
            double rendimento = montante - this.caixinha;
            this.caixinha = montante;
            System.out.printf("REndimento de caixinha após %d meses: RS%.2f\n", this.tempo_investimento, rendimento);
        } else {
            System.out.println("Não há investimento ou caixinha manor que 0.");
        }
    }

    // Método de extrato
    public void extrato() {
        System.out.println(
            "---------------------------------------------------------------------\n"+
            "Conta "+ this.conta +" \n"+
            "Agencia "+ this.agencia+ "\n"+
            "Saldo "+ String.format("%2f", this.saldo) +"\n"+
            "Cliente "+ this.cliente+"\n"+
            "---------------------------------------------------------------------\n"
        );
    }

    public static void main(String[] args) throws InterruptedException {
        Banco cliente1 = new Banco("Moeda Saqua", "0001", 1234562, "Ze da Manga", "12345678900");
        cliente1.definirsenha("admin");
        cliente1.deposito(5000);
        cliente1.caixinha_invest(2500, 12);
        cliente1.extrato();

        // simular que passou 12 meses
        System.out.println("12 meses depois.......");
        Thread.sleep(20);
        cliente1.calular_rendimento();
        cliente1.extrato();

        //Simulando outro cliente
        Banco clinete2 = new Banco("BAnco invest", "0005", 32165498, "Zé das Coves", "98765432102");
        clinete2.definirsenha("123");
        clinete2.deposito(150);

        cliente1.pix(clinete2, 1500);

        cliente1.extrato();

        clinete2.extrato();
    }

}