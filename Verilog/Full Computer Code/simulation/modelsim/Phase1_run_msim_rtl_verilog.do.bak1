transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -vlog01compat -work work +incdir+C:/Users/789wi/Videos/ELEC-374 {C:/Users/789wi/Videos/ELEC-374/boothMultiplier.v}
vlog -vlog01compat -work work +incdir+C:/Users/789wi/Videos/ELEC-374 {C:/Users/789wi/Videos/ELEC-374/twoCompliment.v}

vlog -vlog01compat -work work +incdir+C:/Users/789wi/Videos/ELEC-374 {C:/Users/789wi/Videos/ELEC-374/TestbenchMultiplier.v}

vsim -t 1ps -L altera_ver -L lpm_ver -L sgate_ver -L altera_mf_ver -L altera_lnsim_ver -L cycloneiii_ver -L rtl_work -L work -voptargs="+acc"  TestbenchMultiplier

add wave *
view structure
view signals
run 500 ns
