public class Main {

    interface State {
        void enter();
        void execute();
        void leave();
        String getName();
    }

    static class AgentA {
        State state;
        int timer = 0;
        int health = 100;
        boolean enemyDetected = false;

        AgentA() {
            state = new Patrolling(this);
            state.enter();
        }

        void update() {
            state.execute();
        }

        void changeState(State next) {
            state.leave();
            System.out.println("[A] " + state.getName() + " -> " + next.getName());
            state = next;
            state.enter();
        }

        void resetTimer() {
            timer = 0;
        }
    }

    static class Patrolling implements State {
        AgentA a;

        Patrolling(AgentA a) {
            this.a = a;
        }

        @Override
        public void enter() {
            a.resetTimer();
            System.out.println("[A] Começou a patrulhar.");
        }

        @Override
        public void execute() {
            a.timer++;
            System.out.println("[A] Patrulhando: " + a.timer);

            if (a.enemyDetected || a.timer >= 5)
                a.changeState(new Alert(a));
        }

        @Override
        public void leave() {
            System.out.println("[A] Parou de patrulhar.");
        }

        @Override
        public String getName() {
            return "PATROLLING";
        }
    }

    static class Alert implements State {
        AgentA a;

        Alert(AgentA a) {
            this.a = a;
        }

        @Override
        public void enter() {
            a.resetTimer();
            System.out.println("[A] Entrou em alerta.");
        }

        @Override
        public void execute() {
            a.timer++;
            System.out.println("[A] Verificando área: " + a.timer);

            if (a.enemyDetected)
                a.changeState(new Combat(a));
            else if (a.timer >= 3)
                a.changeState(new Patrolling(a));
        }

        @Override
        public void leave() {
            System.out.println("[A] Saiu do alerta.");
        }

        @Override
        public String getName() {
            return "ALERT";
        }
    }

    static class Combat implements State {
        AgentA a;

        Combat(AgentA a) {
            this.a = a;
        }

        @Override
        public void enter() {
            a.resetTimer();
            System.out.println("[A] Entrou em combate!");
        }

        @Override
        public void execute() {
            a.timer++;
            System.out.println("[A] Combatendo: " + a.timer);

            if (a.timer % 2 == 0) {
                a.health -= 10;
                System.out.println("[A] Vida: " + a.health);
            }

            if (a.health <= 50) {
                a.changeState(new Retreat(a));
            } 
            else if (a.timer >= 4) {
                System.out.println("[A] Inimigo derrotado!");
                a.enemyDetected = false;
                a.changeState(new Patrolling(a));
            }
        }

        @Override
        public void leave() {
            System.out.println("[A] Saiu do combate.");
        }

        @Override
        public String getName() {
            return "COMBAT";
        }
    }

    static class Retreat implements State {
        AgentA a;

        Retreat(AgentA a) {
            this.a = a;
        }

        @Override
        public void enter() {
            a.resetTimer();
            System.out.println("[A] Recuando.");
        }

        @Override
        public void execute() {
            a.timer++;
            System.out.println("[A] Recuando: " + a.timer);

            if (a.timer >= 3) {
                a.health = Math.min(100, a.health + 20);
                a.enemyDetected = false;
                a.changeState(new Patrolling(a));
            }
        }

        @Override
        public void leave() {
            System.out.println("[A] Terminou a retirada.");
        }

        @Override
        public String getName() {
            return "RETREAT";
        }
    }

    static class AgentB {
        State state;
        int timer = 0;
        AgentA agentA;

        AgentB(AgentA agentA) {
            this.agentA = agentA;
            state = new Searching(this);
            state.enter();
        }

        void update() {
            state.execute();
        }

        void changeState(State next) {
            state.leave();
            System.out.println("[B] " + state.getName() + " -> " + next.getName());
            state = next;
            state.enter();
        }

        void resetTimer() {
            timer = 0;
        }
    }

    static class Searching implements State {
        AgentB b;

        Searching(AgentB b) {
            this.b = b;
        }

        @Override
        public void enter() {
            b.resetTimer();
            System.out.println("[B] Procurando inimigos.");
        }

        @Override
        public void execute() {
            b.timer++;
            System.out.println("[B] Procurando: " + b.timer);

            if (b.timer >= 3) {
                System.out.println("[B] Inimigo localizado!");
                b.changeState(new Tracking(b));
            }
        }

        @Override
        public void leave() {
            System.out.println("[B] Terminou a busca.");
        }

        @Override
        public String getName() {
            return "SEARCHING";
        }
    }

    static class Tracking implements State {
        AgentB b;

        Tracking(AgentB b) {
            this.b = b;
        }

        @Override
        public void enter() {
            b.resetTimer();
            System.out.println("[B] Rastreando inimigo.");
        }

        @Override
        public void execute() {
            b.timer++;
            System.out.println("[B] Rastreando: " + b.timer);

            if (b.timer >= 2) {
                System.out.println("[B] Enviando localização para A.");

                b.agentA.enemyDetected = true;

                b.changeState(new Supporting(b));
            }
        }

        @Override
        public void leave() {
            System.out.println("[B] Parou de rastrear.");
        }

        @Override
        public String getName() {
            return "TRACKING";
        }
    }

    static class Supporting implements State {
        AgentB b;

        Supporting(AgentB b) {
            this.b = b;
        }

        @Override
        public void enter() {
            b.resetTimer();
            System.out.println("[B] Entrou em suporte.");
        }

        @Override
        public void execute() {
            b.timer++;
            System.out.println("[B] Dando suporte: " + b.timer);

            if (b.timer >= 4) {
                System.out.println("[B] Suporte finalizado.");
                b.changeState(new Searching(b));
            }
        }

        @Override
        public void leave() {
            System.out.println("[B] Saiu do suporte.");
        }

        @Override
        public String getName() {
            return "SUPPORTING";
        }
    }

    static class GameManager {

        AgentA a = new AgentA();
        AgentB b = new AgentB(a);

        void run() {

            for (int tick = 1; tick <= 25; tick++) {

                System.out.println("\n===== TICK " + tick + " =====");

                a.update();
                b.update();
            }

            System.out.println("\n===== FIM DA SIMULAÇÃO =====");
        }
    }

    public static void main(String[] args) {
        GameManager game = new GameManager();
        game.run();
    }
}