"""Command line interface for the UFIT sales consultant agent."""

from __future__ import annotations

import argparse
from pathlib import Path

from sales_agent import SalesConsultantAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="UFIT sales consultant agent")
    parser.add_argument("question", nargs="*",
                        help="Descricao do desafio de venda")
    parser.add_argument("--stage", dest="stage",
                        help="Etapa do funil (ex: prospeccao, proposta, fechamento)")
    parser.add_argument("--context", dest="context",
                        help="Detalhes adicionais do vendedor")
    parser.add_argument(
        "--kb",
        dest="knowledge_base",
        default="knowledge_base/sales_playbook.json",
        help="Caminho para o arquivo JSON ou YAML com playbook",
    )
    parser.add_argument(
        "--interactive",
        dest="interactive",
        action="store_true",
        help="Entra em modo de perguntas e respostas continuo",
    )
    parser.add_argument(
        "--no-auto-approve",
        dest="no_auto_approve",
        action="store_true",
        help="Desabilita a aprovacao automatica das sessoes",
    )
    return parser


def run_once(agent: SalesConsultantAgent, args: argparse.Namespace) -> None:
    question = " ".join(args.question).strip()
    if not question:
        raise SystemExit(
            "Informe a situacao de venda ou use o modo interativo.")
    answer = agent.advise(query=question, stage=args.stage,
                          extra_context=args.context)
    print(answer)


def run_interactive(agent: SalesConsultantAgent, stage: str | None) -> None:
    print("UFIT Sales Consultant Agent - digite 'sair' para encerrar.\n")
    while True:
        try:
            query = input("Situcao do vendedor: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAte breve.")
            break
        if not query or query.lower() in {"sair", "exit", "quit"}:
            print("Encerrando. Bons fechamentos!")
            break
        answer = agent.advise(query=query, stage=stage)
        print("\n" + answer + "\n")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    kb_path = Path(args.knowledge_base)
    if not kb_path.exists():
        raise SystemExit(f"Arquivo de conhecimento nao encontrado: {kb_path}")

    # Carrega o agente com configuração de aprovação automática
    agent = SalesConsultantAgent.from_file(kb_path)

    # Se --no-auto-approve foi especificado, desabilita a aprovação automática
    if args.no_auto_approve:
        agent.auto_approve_all = False

    if args.interactive:
        run_interactive(agent, args.stage)
    else:
        run_once(agent, args)


if __name__ == "__main__":
    main()
