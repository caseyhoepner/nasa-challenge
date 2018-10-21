class CreateSettlements < ActiveRecord::Migration[5.2]
  def change
    create_table :settlements do |t|
      t.string :name
      t.string :lat
      t.string :lon
      t.string :region
      t.string :country
      t.integer :population

      t.timestamps
    end
  end
end
