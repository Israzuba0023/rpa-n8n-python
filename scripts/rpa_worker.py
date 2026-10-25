cat << 'EOF' > scripts/rpa_worker.py
import json
import sys
import datetime

def process_rpa_task(payload=None):
    """
    Função principal do worker de RPA.
    Processa dados recebidos e simula uma execução automatizada.
    """
    timestamp = datetime.datetime.now().isoformat()
    
    # Processamento dos dados
    result = {
        "status": "success",
        "timestamp": timestamp,
        "message": "Processo de RPA executado com sucesso pelo Worker Python.",
        "payload_recebido": payload if payload else {}
    }
    
    return result

if __name__ == "__main__":
    try:
        # Lê argumentos do terminal se enviados
        input_data = {}
        if len(sys.argv) > 1:
            input_data = json.loads(sys.argv[1])
            
        output = process_rpa_task(input_data)
        print(json.dumps(output, indent=2))
        sys.exit(0)
    except Exception as e:
        error_output = {
            "status": "error",
            "message": f"Erro durante a execução do RPA: {str(e)}"
        }
        print(json.dumps(error_output, indent=2), file=sys.stderr)
        sys.exit(1)
EOF
