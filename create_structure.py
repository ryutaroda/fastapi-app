# docker-compose exec web python create_structure.py

# import os
# from pathlib import Path
#
#
# def create_ddd_structure():
#     base_dir = Path(__file__).parent  # スクリプトのあるディレクトリを基準にする
#
#     directories = [
#         "ddd/domain/item",
#         "ddd/domain/user",
#         "ddd/infra/sqlalchemy/item",
#         "ddd/infra/sqlalchemy/user",
#         "ddd/usecase/item",
#         "ddd/presentation/schema/item",
#         "ddd/presentation/schema/user",
#         "routers"
#     ]
#
#     files = {
#         "ddd/domain/item": ["entity.py", "repository.py", "value_objects.py", "exceptions.py"],
#         "ddd/domain/user": ["entity.py", "repository.py", "value_objects.py"],
#         "ddd/infra/sqlalchemy/item": ["repository.py"],
#         "ddd/infra/sqlalchemy/user": ["repository.py"],
#         "ddd/usecase/item": ["model.py", "query_model.py", "query_service.py", "usecase.py"],
#         "ddd/presentation/schema/item": ["purchase.py"],
#         "ddd/presentation/schema/user": ["create.py", "read.py"],
#         "routers": ["item.py", "user.py"]
#     }
#
#     # ディレクトリ作成
#     for directory in directories:
#         os.makedirs(base_dir / directory, exist_ok=True)
#
#     # ファイル作成
#     for directory, filenames in files.items():
#         for filename in filenames:
#             filepath = base_dir / directory / filename
#             if not filepath.exists():
#                 filepath.touch()
#
#
# if __name__ == "__main__":
#     create_ddd_structure()
