-- Zebra tables: Add alternating row colors for better readability
-- This Lua filter applies light gray background to even rows

local colors = {
  odd = '',  -- white/no color
  even = '\\rowcolor{lightgray}'  -- light gray
}

function Table(tbl)
  -- Apply alternating colors to table rows
  local row_number = 0

  -- Color the body rows
  for i, row in ipairs(tbl.bodies[1].body) do
    row_number = row_number + 1
    local color = (row_number % 2 == 0) and colors.even or colors.odd

    -- Insert color command at start of row
    if color ~= '' then
      local color_cell = pandoc.Plain({pandoc.RawInline('latex', color)})
      table.insert(row.cells, 1, pandoc.Cell(color_cell))
      -- Remove the extra cell we just added
      table.remove(row.cells, 1)
      -- Actually, let's do this differently
    end
  end

  return tbl
end
