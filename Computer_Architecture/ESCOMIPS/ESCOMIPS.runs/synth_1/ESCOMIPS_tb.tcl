# 
# Synthesis run script generated by Vivado
# 

set TIME_start [clock seconds] 
proc create_report { reportName command } {
  set status "."
  append status $reportName ".fail"
  if { [file exists $status] } {
    eval file delete [glob $status]
  }
  send_msg_id runtcl-4 info "Executing : $command"
  set retval [eval catch { $command } msg]
  if { $retval != 0 } {
    set fp [open $status w]
    close $fp
    send_msg_id runtcl-5 warning "$msg"
  }
}
create_project -in_memory -part xc7a100tcsg324-1

set_param project.singleFileAddWarning.threshold 0
set_param project.compositeFile.enableAutoGeneration 0
set_param synth.vivado.isSynthRun true
set_property webtalk.parent_dir {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.cache/wt} [current_project]
set_property parent.project_path {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.xpr} [current_project]
set_property default_lib xil_defaultlib [current_project]
set_property target_language Verilog [current_project]
set_property ip_output_repo {c:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.cache/ip} [current_project]
set_property ip_cache_permissions {read write} [current_project]
read_vhdl -library xil_defaultlib {
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/ALU/ALU_1bit.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/ALU/ALU_Nbits.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/ArchivoRegistro/ArchivodeRegistros.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/ArchivoRegistro/BarrelShifter.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/ArchivoRegistro/Demux.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/ESCOMIPS.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/MemoriaDatos/MemoriaDatos.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/Pila_MemoriaPrograma/MemoriaPrograma.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/ArchivoRegistro/Multiplexor_16ch.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/Mux2a1_16bits.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/Mux2a1_4bits.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/Pila_MemoriaPrograma/Pila.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/Pila_MemoriaPrograma/Pila_MemoriaPrograma.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/ArchivoRegistro/Registro.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/Registro_clr.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/UnidadControl/UC_CartaASM.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/UnidadControl/UC_Condicion.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/UnidadControl/UC_DeocdificadorInstruccion.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/UnidadControl/UC_MicrocodigoFuncion.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/UnidadControl/UC_MicrocodigoOpcode.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/UnidadControl/UC_MuxSdopc.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/UnidadControl/UC_MuxSm.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/UnidadControl/UC_Nivel.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/UnidadControl/UC_RegistroEstados.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/UnidadControl/UnidadControl.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/extDireccion.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/extSigno.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/ALU/suma1.vhd}
  {C:/Users/146261/Documents/IPN ESCOM/Arquitectura de Computadoras/ESCOMIPS/ESCOMIPS.srcs/sources_1/new/ESCOMIPS_tb.vhd}
}
# Mark all dcp files as not used in implementation to prevent them from being
# stitched into the results of this synthesis run. Any black boxes in the
# design are intentionally left as such for best results. Dcp files will be
# stitched into the design at a later time, either when this synthesis run is
# opened, or when it is stitched into a dependent implementation run.
foreach dcp [get_files -quiet -all -filter file_type=="Design\ Checkpoint"] {
  set_property used_in_implementation false $dcp
}
set_param ips.enableIPCacheLiteLoad 1
close [open __synthesis_is_running__ w]

synth_design -top ESCOMIPS_tb -part xc7a100tcsg324-1


# disable binary constraint mode for synth run checkpoints
set_param constraints.enableBinaryConstraints false
write_checkpoint -force -noxdef ESCOMIPS_tb.dcp
create_report "synth_1_synth_report_utilization_0" "report_utilization -file ESCOMIPS_tb_utilization_synth.rpt -pb ESCOMIPS_tb_utilization_synth.pb"
file delete __synthesis_is_running__
close [open __synthesis_is_complete__ w]