from src.metaphor_detection import detect_metaphors
from src.sutragama_logic import infer_from_sutragama
from src.karmic_rl import KarmicRL
from src.yuga_cycle_ai import YugaAI

def main():
    print("🔹 Metaphor Detection Test:")
    print(detect_metaphors("Life is a journey, not a destination."))

    print("\n🔹 Sutragama Logic Test:")
    print(infer_from_sutragama("Atman"))

    print("\n🔹 Karmic RL Test:")
    ai = KarmicRL()
    print(f"Karma after action (help): {ai.take_action('help')}")

    print("\n🔹 Yuga Cycle AI Test:")
    yuga_ai = YugaAI()
    print(f"AI Mode in Dvapara Yuga: {yuga_ai.get_ai_mode('Dvapara Yuga')}")

if __name__ == "__main__":
    main()
main.py
