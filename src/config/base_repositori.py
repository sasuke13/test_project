from dataclasses import dataclass

from auto_dataclass.dj_model_to_dataclass import FromOrmToDataclass


class BaseTestRepository:
    def _sort_by_date_and_name(self, querry_set, divided_querry_set_dict: dict, dto: dataclass):
        converter = FromOrmToDataclass()

        for instance in querry_set:
            instance_date_string = str(instance.date)
            if instance_date_string not in divided_querry_set_dict:
                divided_querry_set_dict.update({instance_date_string: []})

            if not divided_querry_set_dict[instance_date_string]:
                (divided_querry_set_dict[instance_date_string].
                 append({instance.name: [converter.to_dto(instance, dto)]}))

            for item in divided_querry_set_dict[instance_date_string]:
                if instance.name in item.keys():
                    item[instance.name].append(converter.to_dto(instance, dto))
                else:
                    item.update({instance.name: [converter.to_dto(instance, dto)]})

    def _sort_by_date(self, querry_set, divided_querry_set_dict: dict, dto: dataclass):
        converter = FromOrmToDataclass()

        for instance in querry_set:
            instance_date_string = str(instance.date)
            if instance_date_string not in divided_querry_set_dict:
                divided_querry_set_dict.update({instance_date_string: []})

            divided_querry_set_dict[instance_date_string].append(converter.to_dto(instance, dto))

    def _sort_by_name(self, querry_set, divided_querry_set_dict: dict, dto: dataclass):
        converter = FromOrmToDataclass()

        for instance in querry_set:
            if instance.name not in divided_querry_set_dict:
                divided_querry_set_dict.update({instance.name: []})

            divided_querry_set_dict[instance.name].append(converter.to_dto(instance, dto))
