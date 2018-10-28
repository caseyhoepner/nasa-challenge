class CreateWaterConditions < ActiveRecord::Migration[5.2]
  def change
    create_table :water_conditions do |t|
      t.references :settlement, foreign_key: true
      t.float :cons_use
      t.string :baseline_stress
      t.string :drought_severity
      t.string :flood_occurence
      t.float :total_withdrawl
      t.float :blue_water
      t.string :variability
      t.string :access

      t.timestamps
    end
  end
end
